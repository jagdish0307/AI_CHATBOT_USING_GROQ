# app.py
import streamlit as st
from utils.chat_utils import create_conversation
from utils.session import initialize_session_state

def run_simple_chat():
    initialize_session_state()

    st.title("Simple Groq Chat App")
    model = st.sidebar.selectbox('Choose a model', ['mixtral-8x7b-32768', 'deepseek-r1-distill-qwen-32b'])
    memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, 5)

    conversation = create_conversation(model, memory_length)

    user_question = st.text_area("Ask a question:")
    if user_question:
        response = conversation(user_question)
        st.session_state.chat_history.append({'human': user_question, 'AI': response['response']})
        st.write("Chatbot:", response['response'])

if __name__ == "__main__":
    run_simple_chat()
