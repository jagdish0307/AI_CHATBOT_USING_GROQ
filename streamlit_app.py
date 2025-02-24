import streamlit as st
from datetime import datetime
from utils.session import initialize_session_state
from utils.chat_utils import create_conversation
from utils.prompts import get_custom_prompt

def run_app():
    initialize_session_state()

    # Sidebar Configuration
    with st.sidebar:
        st.title("🛠️ Chat Settings")
        model = st.selectbox('Choose your model:', ['mixtral-8x7b-32768', 'deepseek-r1-distill-qwen-32b'])
        memory_length = st.slider('Conversation Memory (messages)', 1, 10, 5)
        st.session_state.selected_persona = st.selectbox('Select conversation style:', ['Default', 'Expert', 'Creative'])

        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.start_time = None
            st.rerun()

    # Main Chat Interface
    st.title("🤖 Groq Chat Assistant")
    prompt_template = get_custom_prompt(st.session_state.selected_persona)
    conversation = create_conversation(model, memory_length, prompt_template)

    # Display Chat History (Sequential from Top to Bottom)
    for message in st.session_state.chat_history:  # Display from top to bottom
        with st.chat_message("user"):
            st.markdown(f"{message['human']}")
        with st.chat_message("assistant"):
            st.markdown(f"{message['AI']}")

    # Input Box at the Bottom
    with st.container():
        st.markdown("---")
        user_question = st.chat_input("💬 Type your message here...")

        if user_question:
            if not st.session_state.start_time:
                st.session_state.start_time = datetime.now()
            response = conversation(user_question)
            st.session_state.chat_history.append({'human': user_question, 'AI': response['response']})
            st.rerun()  # Refresh to show the latest message at the bottom

if __name__ == "__main__":
    run_app()

