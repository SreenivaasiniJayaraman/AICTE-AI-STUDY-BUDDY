import streamlit as st
import random
import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart AI Study Assistant", page_icon="🤖", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.chat-user {
    background-color: #DCF8C6;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}
.chat-ai {
    background-color: #F1F0F0;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙ Settings")

theme = st.sidebar.radio("Theme Mode", ["Light", "Dark"])
mood = st.sidebar.selectbox("Your Mood", ["😊 Happy", "😐 Neutral", "😟 Stressed", "😴 Tired"])

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.chat_history = []

# Download Chat
if "chat_history" in st.session_state and st.session_state.chat_history:
    chat_text = ""
    for sender, msg, time in st.session_state.chat_history:
        chat_text += f"{sender} ({time}): {msg}\n"
    st.sidebar.download_button("⬇ Download Chat", chat_text, file_name="chat_history.txt")

st.sidebar.markdown("---")
st.sidebar.info("Offline AI Assistant | No API Required")

# ---------------- TITLE ----------------
st.title("🤖 Smart AI Study Assistant")
st.markdown("Dynamic AI-like academic chatbot (Offline Mode)")

# ---------------- SESSION ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- AI LOGIC ----------------
def generate_response(question):
    question = question.lower()

    knowledge_base = {
        "operating system": [
            "An operating system manages computer hardware and software.",
            "It handles memory, processes, files, and security.",
            "Examples include Windows, Linux, and macOS."
        ],
        "python": [
            "Python is a high-level programming language used in AI and web development.",
            "Python supports object-oriented programming.",
            "It is popular for data science and automation."
        ],
        "ai": [
            "Artificial Intelligence enables machines to simulate human intelligence.",
            "AI includes machine learning and deep learning.",
            "AI systems learn patterns from data."
        ],
        "database": [
            "A database stores structured data electronically.",
            "SQL is used to manage relational databases.",
            "Examples include MySQL and PostgreSQL."
        ],
        "network": [
            "Computer networks connect devices to share resources.",
            "Common types include LAN, WAN, and MAN.",
            "Protocols like TCP/IP manage communication."
        ]
    }

    for key in knowledge_base:
        if key in question:
            return random.choice(knowledge_base[key])

    return f"This topic about '{question}' involves theory, practical implementation, and real-world applications."

# ---------------- QUICK SUGGESTIONS ----------------
st.markdown("### 🔎 Quick Topics")
col1, col2, col3 = st.columns(3)

if col1.button("Operating System"):
    user_input = "Explain operating system"
elif col2.button("Python"):
    user_input = "Tell me about python"
elif col3.button("Artificial Intelligence"):
    user_input = "Explain AI"
else:
    user_input = st.text_input("Ask your academic question:")

# ---------------- SEND BUTTON ----------------
if st.button("Send"):
    if user_input.strip() != "":
        time = datetime.datetime.now().strftime("%H:%M")

        st.session_state.chat_history.append(("You", user_input, time))

        with st.spinner("🤖 AI is thinking..."):
            response = generate_response(user_input)

        st.session_state.chat_history.append(("AI", response, time))

# ---------------- DISPLAY CHAT ----------------
st.markdown("### 💬 Conversation")

for sender, message, time in st.session_state.chat_history:
    if sender == "You":
        st.markdown(
            f"<div class='chat-user'><b>You ({time}):</b><br>{message}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-ai'><b>AI ({time}):</b><br>{message}</div>",
            unsafe_allow_html=True
        )

st.markdown("---")
st.caption("Smart AI Study Assistant | Interactive UI | Offline AI Simulation")
