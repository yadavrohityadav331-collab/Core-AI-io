import streamlit as st

# Page Configuration
st.set_page_config(page_title="CORE AI", page_icon="🤖")

# Simple CSS for better look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_index=True)

# App Content
st.title("🤖 CORE AI")
st.subheader("Developed by Rohit Yadav")
st.write("Welcome back, Rohit bhai! CORE AI is officially online.")

# Chat System
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Kaise ho Rohit bhai?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = f"Rohit bhai, main aapka personal 'CORE AI' hoon. Aapne pucha: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
