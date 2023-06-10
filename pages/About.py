import streamlit as st
import os
from streamlit_lottie import st_lottie


st.title('About')
st.info('This is the about page for the product comparison app')

st.header('Team Members')
team_cols = st.columns(3)
with team_cols[0]:
    st.image(
        'https://media.licdn.com/dms/image/D5603AQGSG4Ue2mb-Jw/profile-displayphoto-shrink_800_800/0/1686028976153?e=1691625600&v=beta&t=9ombaR4hYZkPSn0MvXgD1dmHrLWQ3WiPUBJwoTV6cEY', 
        caption='Suchat T',clamp=True)
    
    st.write('Team Leader/Developer')
    st.write('[LinkedIn](https://www.linkedin.com/in/suchat-tangjarukij-173707153/)')
            
with team_cols[1]:
    st.image(
        'https://media.licdn.com/dms/image/C4D03AQEaPkfqJ-gKig/profile-displayphoto-shrink_800_800/0/1657097273988?e=1691625600&v=beta&t=M5oxj0XVcR3mLVriimX-loWgFws13oC6ByG1gxYwrZ8', 
        caption='Nattiya N'
        )
    st.write('Creative/Developer')
    st.write('[LinkedIn](https://www.linkedin.com/in/nattiya-nattrakulpithak-6a3020191/)')

with team_cols[2]:
    st.image(
        'https://media.licdn.com/dms/image/C5103AQFCbbtxONV7MA/profile-displayphoto-shrink_800_800/0/1526556695732?e=1691625600&v=beta&t=gnc6C2B0NW8izTpkio8efzK7KBIe10AcLoW8IHcLQnw', 
        caption='Chanawee C'
        )
    st.write('Creative/Developer')
    st.write('[LinkedIn](https://www.linkedin.com/in/chanawee/)')

## Problem Statement
st.markdown('''
## Problem Statement

In today's digital age, consumers face the daunting task of comparing numerous products before making a purchase decision. The overwhelming amount of information available online often leads to information overload, making it difficult for consumers to gather and analyze relevant data efficiently. As a result, they may struggle to make informed decisions and end up with products that don't meet their needs.
''')


## Solution Overview
cols =  st.columns(2)
with cols[0]:
    st.markdown('''
## Solution Overview
To address this problem, we have developed an AI agent that leverages cutting-edge technologies, including Langchain and Streamlit, to revolutionize the product comparison process. Our AI agent acts as a virtual assistant, sifting through vast amounts of data from various sources and generating comprehensive and user-friendly comparison articles.
    ''')

with cols[1]:
    st_lottie("https://assets2.lottiefiles.com/packages/lf20_cuKhxGQKFB.json")


## Features
st.markdown('''
## Key Features
''')
            
cols = st.columns(2)
with cols[0]:
    st.markdown('''
### Natural Language Processing

Our AI agent utilizes Langchain's advanced language processing capabilities to extract relevant information from product descriptions, reviews, and specifications. This ensures accurate and comprehensive data analysis.
'''            
    )

with cols[1]:
    st.markdown('''
### Data Aggregation

By aggregating data from multiple sources, our AI agent provides a holistic view of each product. This saves consumers valuable time and effort by eliminating the need to visit numerous websites and read through multiple reviews.
''')

cols = st.columns(2)
with cols[0]:
    st.markdown('''
### Customizable Criteria

We understand that every consumer has unique preferences and priorities. Our AI agent allows users to define their own criteria for comparison, ensuring that the generated articles align with their specific needs.
'''
    )

with cols[1]:
    st.markdown('''
### Streamlined Interface

Powered by Streamlit, our web app framework of choice, our AI agent offers a seamless and intuitive user experience. The interface is designed to be user-friendly and interactive, enabling consumers to navigate and explore comparison articles effortlessly.
''')    

## Roadmap
st.markdown('''
## Roadmap

We have an exciting roadmap ahead, aiming to continuously enhance our AI agent's capabilities and expand its reach. Some of our planned future features include:
''')     
cols = st.columns(2)


with cols[0]:
    st_lottie("https://assets4.lottiefiles.com/packages/lf20_NIqx0dKgO5.json")
with cols[1]:
    st.markdown('''
    1. Creation of AI agent to collect data from the internet and analyse.
    2. Integration with additional e-commerce platforms, allowing users to directly compare products from their favorite online stores.
    3. Sentiment analysis to provide users with insights into customer satisfaction and opinions.
    4. Mobile app development to extend our AI agent's accessibility and convenience.
    ''')
            


# load mardown file
with open("./pages/src/about.md", "r") as f:
    about_md = f.read()
    st.markdown(about_md)

