import streamlit as st
from dotenv import dotenv_values
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.prompts.chat import ChatPromptTemplate

env_variables = dotenv_values('.env')
openai_key = env_variables['OPEN_AI_API_KEY']
print(openai_key)
# archivo con prompt
f = open('prompt.txt', 'r')
template = f.read()
f.close()

chat = ChatOpenAI(openai_api_key=openai_key, temperature=0.2, model='gpt-3.5-turbo', max_tokens=2048)
prompt_template = ChatPromptTemplate.from_template(template)
# loader = TextLoader('plan.csv')
loader = DirectoryLoader('csv/', glob="**/*.csv", loader_cls=TextLoader)
docs = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
vectors = FAISS.from_documents(docs, embeddings)
chain = ConversationalRetrievalChain.from_llm(llm=chat, retriever=vectors.as_retriever())


def conversational_chat(query):
    response = chain({"question": query, "chat_history": st.session_state['history'][-5:]})
    messages = response["answer"].split("\n")
    for msg in messages:
        st.session_state['history'].append((query, msg))

    return response["answer"]


if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hola! Bienvenido al chat de Entel. ¿En que te puedo ayudar?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hola ! 👋"]

# container for the chat history
response_container = st.container()
# container for the user's text input
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input('', placeholder="Escribe tus consultas aquí", key='input')
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output = conversational_chat(user_input)

        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="thumbs")
            message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
