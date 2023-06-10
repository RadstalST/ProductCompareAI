# create streamlit app



import pandas as pd
import numpy as np
import streamlit as st

from AI.agent import Agent



with st.sidebar:
    OPEN_AI_API_KEY = st.text_input('OPEN AI KEY',type="password")

if OPEN_AI_API_KEY:
    agent = Agent(openai_api_key=OPEN_AI_API_KEY)

@st.cache_data #caching the function
def execute_agent(prompt):
	#agent = Agent(openai_api_key=OPEN_AI_API_KEY)
    agent_res = agent.execute(prompt)
    return agent_res


# Title of the app
st.title('Product Comparison')

st.info('This app compares the products based on the features')

#input
with st.form(key='input_form'):
    product1 = st.text_input('Enter the name of the product 1',value="apple vision pro")
    product2 = st.text_input('Enter the name of the product 2',value="Meta Quest Pro")
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
    with st.expander("Debug"):
        st.write(agent_res)

    # introduction section

    st.title(f"{agent_res['title']}")

    st.header(f"Introduction :") #might add catchy clickbait title
    st.write(agent_res["introduction"])
    st.header(f"{product1} vs {product2}") #might add catchy clickbait title
    st.write(agent_res["vs_paragraph"])
    st.header(f"Features Comparison Table") 
    st.write(f"Here is the comparison between {product1} and {product2}")
    # comparison section
    st.markdown(agent_res["features_table"].strip())



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
