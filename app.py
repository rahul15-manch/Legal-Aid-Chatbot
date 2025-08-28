import streamlit as st
from langchain_community.chat_models import ChatOllama  # or ChatOpenAI, ChatGroq

# ---------- Page Setup ----------
st.set_page_config(page_title="Legal Aid Chatbot", layout="wide")

# ---------- Session State for History ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- Sidebar (History) ----------
with st.sidebar:
    st.title("📜 Chat History")
    if st.session_state.history:
        for i, chat in enumerate(st.session_state.history, 1):
            with st.expander(f"Chat {i}"):
                st.markdown(f"**🧑 You:** {chat['question']}")
                st.markdown(f"**🤖 Bot:** {chat['answer']}")
    else:
        st.info("No history yet. Ask something!")

# ---------- Main Chat UI ----------
st.title("⚖️ Legal Aid Chatbot")

# Define LLM
llm = ChatOllama(model="llama3")

# Input area
query = st.chat_input("Ask a legal question...")

if query:
    # Show user query
    with st.chat_message("user"):
        st.markdown(query)

    # Placeholder for bot response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        # Streaming response
        for chunk in llm.stream(query):
            token = chunk.content if chunk.content else ""
            full_response += token
            placeholder.markdown(full_response)

    # Save to history
    st.session_state.history.append({"question": query, "answer": full_response})
