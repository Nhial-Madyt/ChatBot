import streamlit as st
import openai

my_api = "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"

# Set your OpenAI API key here
openai.api_key = my_api

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("Smart ChatBot")

# Sidebar for system message (subject)
if "system_message" not in st.session_state:
    system_message = st.sidebar.text_input("Enter the subject you'd like to talk about:")
    if system_message:
        st.session_state["system_message"] = system_message
        st.session_state["messages"].append({"role": "system", "content": system_message})
        st.sidebar.success(f"You are now talking about: {system_message}")

# Display chat messages
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Chat input (always visible once system_message is set)
if "system_message" in st.session_state:
    user_input = st.chat_input("Type your message...")

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