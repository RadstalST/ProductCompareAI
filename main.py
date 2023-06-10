# create streamlit app


import streamlit as st
import pandas as pd
import numpy as np
import json
import json5
from AI.agent import Agent



with st.sidebar:
    OPEN_AI_API_KEY = st.text_input('OPEN AI KEY',type="password")

if OPEN_AI_API_KEY:
    agent = Agent(openai_api_key=OPEN_AI_API_KEY)

@st.cache_data #caching the function
def execute_agent(prompt):
    agent_res = agent.execute(prompt)
    return agent_res


# Title of the app
st.title('Product Comparison')

st.info('This app compares the products based on the features')

#input
with st.form(key='input_form'):
    product1 = st.text_input('Enter the name of the product 1')
    product2 = st.text_input('Enter the name of the product 2')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.divider()
    st.write(f'Product 1: {product1}')
    st.write(f'Product 2: {product2}')
    st.write('Comparing the products...')
    prompt = f"compare {product1} and {product2}"
    st.write(prompt)
    st.divider()
    agent_res = execute_agent(prompt)
    st.write(agent_res)

    comparison_df = pd.DataFrame(json5.loads(
        agent_res["features_table"].replace('\'',"\"" ).strip()
        )).set_index("product").T
    
    # st table
    st.table(comparison_df)

    # pro and cons section
    st.subheader("Pros and Cons")
    pros_cons = agent_res["pro_cons"]
    pros_cons_list = pros_cons.split("\n\n")
    for section in pros_cons_list:
        if section.startswith("Pros:"):
            st.subheader("Pros")
            st.write(pros_cons_list[0].replace('Pros:\n',''))
        elif section.startswith("Cons:"):
            st.subheader("Cons")
            st.write(pros_cons_list[1].replace('Pros:\n',''))
            

# go get some data on the internet
