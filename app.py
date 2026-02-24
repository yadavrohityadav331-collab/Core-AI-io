# STEP 1: Setup
!pip install streamlit -q

# STEP 2: Create the fixed App File
with open('app.py', 'w') as f:
    f.write("""
import streamlit as st
import time

# Basic Config
st.set_page_config(page_title="CORE AI", page_icon="🤖")

# Simple Header (Fixed Error)
st.title("🤖 CORE AI")
st.subheader("By Rohit Yadav")
st.write("Your Emotional Friend is ready!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Display
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
if prompt := st.chat_input("Kaise ho Rohit bhai?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = "Main sun raha hoon... 😊 Sab badhiya hoga!"
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
""")

