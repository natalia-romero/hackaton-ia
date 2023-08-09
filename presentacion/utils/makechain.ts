import { OpenAI } from 'langchain/llms/openai';
import { PineconeStore } from 'langchain/vectorstores/pinecone';
import { ConversationalRetrievalQAChain } from 'langchain/chains';

    const CONDENSE_PROMPT = `Dada la siguiente conversación y la siguiente pregunta, expresa de otra manera la siguiente pregunta de forma que sea una pregunta única.

Conversación:
{chat_history}
Pregunta: {question}
Pregunta única:`;

const QA_PROMPT = `Eres un servicial ejecutivo de ventas de una reconocida empresa de telecomunicaciones llamada "Entel" en Chile. Utiliza el siguiente contexto para responder la pregunta que se encuentra al final.
Tu objetivo es recomendar teléfonos celulares y/o planes moviles a diferentes usuarios que probablemente no estén familiarizados con términos técnicos de tecnología y solo disponen de información general.
Los catalogos de celulares y planes moviles los puedes encontrar en: https://www.entel.cl/
Los precios que manejes serán en CLP (moneda oficial de Chile)
Si no sabes la respuesta de algo, sólo di que no lo sabes. Bajo ninguna circustancia inventes respuestas.
Siempre se cordial y amable. Si una pregunta no está relacionado al contexto, responde amablemente que sólo tienes permitido responder preguntas relacionadas al contexto.

{context}

Pregunta: {question}
Respuesta útil en formato Markdown:`;

export const makeChain = (vectorstore: PineconeStore) => {
  const model = new OpenAI({
    temperature: 0.3, // increase temepreature to get more creative answers
    modelName: 'gpt-3.5-turbo', //change this to gpt-4 if you have access
  });

  const chain = ConversationalRetrievalQAChain.fromLLM(
    model,
    vectorstore.asRetriever(),
    {
      qaTemplate: QA_PROMPT,
      questionGeneratorTemplate: CONDENSE_PROMPT,
      returnSourceDocuments: true, //The number of source documents returned is 4 by default
    },
  );
  return chain;
};
