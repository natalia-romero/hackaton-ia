from dotenv import dotenv_values
import streamlit as st
from judini.agent import Agent

env_variables = dotenv_values('.env')

api_key = env_variables['JUDINI_API_KEY']
agent_id = env_variables['AGENT_ID']

agent = Agent(api_key, agent_id)

prompt = 'Hola'
response = agent.completion(prompt)
print(response)