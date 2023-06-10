import streamlit as st
import os

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


# read /pages/src/about.md and print to screen
with open(os.path.join(os.path.dirname(__file__), "src/about.md"), "r") as f:
    st.markdown(f.read())
