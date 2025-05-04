import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🧠 Simple LLM Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("Please set OPENAI_API_KEY as an environment variable.")
    st.stop()

llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

user_input = st.text_input("You:", key="user_input")
if st.button("Send") and user_input:
    response = conversation.run(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
