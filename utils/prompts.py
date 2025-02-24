# utils/prompts.py
from langchain.prompts import PromptTemplate

def get_custom_prompt(persona):
    """Return persona-based custom prompt template"""
    personas = {
        'Default': """You are a helpful AI assistant.
                     Current conversation:
                     {history}
                     Human: {input}
                     AI:""",
        'Expert': """You are an expert consultant with deep knowledge across multiple fields.
                    Please provide detailed, technical responses when appropriate.
                    Current conversation:
                    {history}
                    Human: {input}
                    Expert:""",
        'Creative': """You are a creative and imaginative AI that thinks outside the box.
                      Feel free to use metaphors and analogies in your responses.
                      Current conversation:
                      {history}
                      Human: {input}
                      Creative AI:"""
    }
    return PromptTemplate(
        input_variables=["history", "input"],
        template=personas[persona]
    )
