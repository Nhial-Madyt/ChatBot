import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("my_api")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("Smart ChatBot")

# Sidebar for system message

if "system_message" not in st.session_state:
    system_message = st.sidebar.title("Hi! my name is Kira I'll be your assistant today (●'◡'●):")
# Display chat messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Chat input always visible once system_message is set
user_input = st.chat_input("Ask anything...")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Display immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Generate AI response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["messages"]
        )
        ai_reply = response.choices[0].message.content

        # Save assistant message
        st.session_state["messages"].append({"role": "assistant", "content": ai_reply})

        # Display assistant reply
        with st.chat_message("assistant"):
            st.markdown(ai_reply)

    except Exception as e:
        st.error(f"An error occurred: {e}")