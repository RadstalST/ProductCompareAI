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
def execute_agent(prompt,budget=0):
	#agent = Agent(openai_api_key=OPEN_AI_API_KEY)
    agent_res = agent.execute(prompt,budget=budget)
    return agent_res

@st.cache_data
def execute_review(prompt):
	rev = agent.review(prompt)
	return rev
@st.cache_data
def execute_review1(prompt):
	rev = agent.review(prompt)
	return rev
@st.cache_data
def execute_specific_feature(prompt):
    specific_feature = agent.feature(prompt)
    return specific_feature

# Title of the app
st.title('Product Comparison')

st.info('This app compares the products based on the features')

#input
with st.form(key='input_form'):
    product1 = st.text_input('Enter the name of the product 1',value="apple vision pro")
    product2 = st.text_input('Enter the name of the product 2',value="Meta Quest Pro")
    feature = st.text_input('Enter specific feature you want to compare',value="optional")
    budget = st.number_input('Enter your budget ($)')
    submit_button = st.form_submit_button(label='Submit')
if not OPEN_AI_API_KEY:
    st.error("Please enter the Open AI API Key")
    st.stop()
if submit_button:
    st.divider()
    st.write(f'Product 1: {product1}')
    st.write(f'Product 2: {product2}')
    budget = float(budget)
    if budget > 0:
        st.write(f'Budget : {budget}$')
    st.write('Comparing the products...')
    prompt = f"compare {product1} and {product2}"
    # if budget > 0:
    #     prompt = f"compare {product1} and {product2} in budget {budget}"
    st.write(prompt)
    st.divider()
    agent_res = execute_agent(prompt,budget=budget)
    with st.expander("Debug"):
        st.write(agent_res)
    # review1 = f"customer review of {product1}"
    # review = execute_review(review1)
    # st.header(f"Customer Review of {product1}")
    # st.write(review["output"])
    # st.divider()
    # st.header(f"Customer Review of {product2}")
    # review2_prompt = f"customer review of {product2}"
    # review2 = execute_review(review2_prompt)
    # st.write(review2["output"])





    #introduction section
    st.title(f"{agent_res['title']}")

    st.header(f"Introduction :") #might add catchy clickbait title
    st.write(agent_res["introduction"])
    st.header(f"{product1} vs {product2}") #might add catchy clickbait title
    st.write(agent_res["vs_paragraph"])
    st.header(f"Features Comparison Table") 
    st.write(f"Here is the comparison between {product1} and {product2}")
    # comparison section
    st.markdown(agent_res["features_table"].strip())
    if feature!='optional':
        st.subheader(f"Compare based on requested feature: {feature}")
        feat_prompt = f"(compare {product1} and {product2} {feature}"
        result_feature = execute_specific_feature(feat_prompt)
        st.write(result_feature["output"])





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

    # budget
    st.subheader("Which one is better in budget")
    budget_consider = agent_res["budget_consider"]
    st.write(budget_consider)

            
    st.divider()
    # reviews section
    review1 = f"customer review of {product1}"
    review = execute_review(review1)
    st.subheader(f"Customer Review of {product1}")
    st.write(review["output"])
    st.subheader(f"Customer Review of {product2}")
    review2_prompt = f"customer review of {product2}"
    review2 = execute_review1(review2_prompt)
    st.write(review2["output"])
