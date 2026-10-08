
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Groq AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Groq AI Chatbot")
st.caption("Powered by Groq + Python + Streamlit")

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Type your message here...")

if user_message:

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):

        response_box = st.empty()
        full_response = ""

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=st.session_state.messages,
            temperature=0.7,
            stream=True
        )

        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                response_box.markdown(full_response + "▌")

        response_box.markdown(full_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })
