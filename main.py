# create streamlit app


import streamlit as st
import pandas as pd
import numpy as np



with st.sidebar:
    OPEN_AI_API_KEY = st.text_input('OPEN AI KEY',type="password")

# Title of the app
st.title('Product Comparison')

st.info('This app compares the products based on the features')

#input

product1 = st.text_input('Enter the name of the product 1')
product2 = st.text_input('Enter the name of the product 2')

# go get some data on the internet
