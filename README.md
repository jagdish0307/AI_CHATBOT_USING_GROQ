# 🚀 Groq Chat Assistant

**Groq Chat Assistant** is an interactive chatbot application built with **Streamlit** that allows users to engage with an AI model in a conversational way. It provides a customizable and dynamic chat experience, making it perfect for various needs—from simple information gathering to expert advice and creative brainstorming.

---

## 🔍 **Features**

### 🎯 AI Model and Persona Selection
- Choose from different AI models for optimal performance based on user preferences.
- Select conversation styles (personas):
  - **Default**: Friendly and helpful AI assistant.
  - **Expert**: Provides in-depth, technical, and detailed responses.
  - **Creative**: Delivers imaginative responses with analogies and creative language.

### 🧠 Contextual Memory
- Remembers recent messages for context-aware responses.
- Customize memory depth to define how many previous messages the chatbot should remember.

### 💬 Clear Chat Interface
- Displays chat history with clear formatting for both user messages and AI responses.
- Options to clear chat history and start new conversations.


### 🔒 Error Handling and Security
- Gracefully handles errors and provides clear feedback.
- Keeps sensitive data secure by loading API keys from environment variables.

---

## ⚙️ **Project Setup**

### 1️⃣ Clone the Repository

```bash
git clone https:your Repository
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv enve
```

### 3️⃣ Activate the Virtual Environment

- **On Windows:**
  ```bash
  .\enve\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source enve/bin/activate
  ```

### 4️⃣ Install Project Requirements

```bash
pip install -r requirements.txt
```

### 5️⃣ Set Up Environment Variables

Create a `.env` file in the root directory and add the following:

```
GROQ_API_KEY=your_api_key
```

### 6️⃣ Run the Project

```bash
streamlit run app.py
```


