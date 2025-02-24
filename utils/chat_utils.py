# utils/chat_utils.py
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from .config import GROQ_API_KEY

def initialize_groq_chat(model_name):
    """Initialize Groq chat with selected model"""
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=model_name
    )

def create_conversation(model_name, memory_length, prompt_template=None):
    """Set up conversation chain with memory and prompt"""
    memory = ConversationBufferWindowMemory(k=memory_length)
    groq_chat = initialize_groq_chat(model_name)

    return ConversationChain(
        llm=groq_chat,
        memory=memory,
        prompt=prompt_template
    )
