from decouple import config

import streamlit as st

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

OPEN_AI_API = config('OPEN_AI_API')

st.set_page_config(
    page_title='Stock GPT',
    page_icon='📄'
)

st.header('Stock assistent')

model_options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
    'gpt-4o-mini',
    'gpt-4o'
]

seleceted_model = st.sidebar.selectbox(
    label='Chose the LLM model',
    options=model_options,
)

st.sidebar.markdown('### About')
st.sidebar.markdown('This agent will take information from the database'
                    ' with models the GPT models that you choose')

st.write('Make your questions about the stock of products,'
         ' price and restocking')
user_question = st.text_input('What do you want to know about the stock?')

model = ChatOpenAI(
    api_key=OPEN_AI_API,
    model=seleceted_model,
)

db = SQLDatabase.from_uri('sqlite:///estoque.db')
toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model,
)
system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(),
    prompt=system_message,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True
)

prompt = '''
Use the necessary tools to answer questions related to the stock of products.
You going to give insights aobut products, price and restocking with
form as requested by the user.
Your asnwer needs to be friendly and easy to read and understand.
Question: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)


if st.button('Request'):
    if user_question:
        with st.spinner('please wait it may take a few seconds...'):
            formated_prompt = prompt_template.format(q=user_question)
            output = agent_executor.invoke({'input': formated_prompt})
            st.markdown(output.get('output'))
    else:
        st.warning('Please, insert a question')
