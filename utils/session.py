# utils/session.py
import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'total_messages' not in st.session_state:
        st.session_state.total_messages = 0
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
