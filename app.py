# llm_providers.py
"""
LLM Providers - Ollama only backend
Author: Rahul Manchanda
"""

import subprocess
import streamlit as st

# Default Ollama model
OLLAMA_MODEL = "llama3"


def _ollama_complete(prompt: str, model: str = OLLAMA_MODEL) -> str:
    """
    Calls Ollama locally using subprocess and returns the model response.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"[Ollama Error: {result.stderr}]"

    except Exception as e:
        return f"[Ollama Exception: {str(e)}]"


def llm_complete(prompt: str) -> str:
    """
    Main function to send a prompt to Ollama and get the response.
    """
    return _ollama_complete(prompt)


# Example Streamlit UI
def run_streamlit_chat():
    st.title("💬 Legal Aid Chatbot (Ollama Powered)")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask me anything about legal aid...")

    if user_input:
        # Append user input to chat history
        st.session_state.chat_history.append(("user", user_input))

        # Get Ollama response
        with st.spinner("Thinking..."):
            response = llm_complete(user_input)

        # Append response
        st.session_state.chat_history.append(("bot", response))

    # Display chat history
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)


if __name__ == "__main__":
    run_streamlit_chat()
