from dotenv import dotenv_values
import streamlit as st
import time
import requests
import json

env_variables = dotenv_values('.env')
api_key = env_variables['JUDINI_API_KEY']
agent_id = env_variables['AGENT_ID']

st.title('Chat Entel 📱')
input_container = st.container()
response_container = st.container()
# se inicializa historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hola! Bienvenido al chat de Entel. ¿En que te "
                                                                  "puedo ayudar?"}]

# se muestran mensajes del historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input del user
if prompt := st.chat_input("¿En que te puedo ayudar?"):
    # se agrega input del user al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    # se muestra el input del user
    with st.chat_message("user"):
        st.markdown(prompt)

    # se muestra el input del assistant
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Judini
        url = 'https://playground.judini.ai/api/v1/agent/'+agent_id
        headers = {"Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer "+api_key}
        data = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        response = requests.post(url, headers=headers, json=data, stream=True)
        raw_data = ''
        tokens = ''
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                raw_data = chunk.decode('utf-8').replace("data: ", '')
                if raw_data != "":
                    lines = raw_data.strip().splitlines()
                    for line in lines:
                        print(line)
                        line = line.strip()
                        if line and line != "[DONE]":
                            try:
                                json_object = json.loads(line) 
                                result = json_object['data']
                                full_response += result
                                time.sleep(0.05)
                                # Se agrega un cursor parpadeante para simular que está escribiendo
                                message_placeholder.markdown(full_response + "▌")
                            except json.JSONDecodeError:
                                print(f'Error al decodificar el objeto JSON en la línea: {line}')
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
