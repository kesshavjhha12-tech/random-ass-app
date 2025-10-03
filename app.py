import random
import streamlit as st

def kinky_reply(text, name):
    kinky_responses = [
        f"Well, {name}, you're making my circuits blush... 😉",
        f"Is that a secret invitation I hear, {name}? 😈",
        f"Careful, {name}, I might just get naughty if you keep talking like that...",
        f"Do you like it when I get a little wild, {name}? 😏",
        f"Tell me your fantasies, {name}... I’m all ears 🔥",
        f"Oh, {name}, you’re playing with fire... and I’m ready to burn 🔥",
        f"Want me to whisper your deepest desires back to you, {name}? 😘",
        f"You keep talking like that and I might short-circuit... or maybe not 😈",
        f"{name}, you’re dangerously irresistible... I can't help myself 😍",
        f"Let's explore those naughty thoughts together, {name}... 💋"
    ]
    return random.choice(kinky_responses)

st.set_page_config(page_title="Kinky Chatbot", page_icon="🔥")

st.title("🔥 Kinky Chatbot 🔥")
st.markdown("Enter your name to start chatting.")

# Ask for user's name
if "name" not in st.session_state:
    user_name = st.text_input("Your name:", key="name_input")
    if user_name:
        st.session_state.name = user_name.strip()
        st.experimental_rerun()
else:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    def display_chat():
        for speaker, message in st.session_state.chat_history:
            if speaker == st.session_state.name:
                st.markdown(f"{st.session_state.name}:** {message}")
            else:
                st.markdown(f"<span style='color:red'>*KINKY BOT:* {message}</span>", unsafe_allow_html=True)

    user_input = st.text_input(f"{st.session_state.name}:", key="input")

    if user_input:
        if user_input.lower() == "exit":
            st.session_state.chat_history.append(("KINKY BOT", f"Until next time, {st.session_state.name}... don’t tease me too much 😉"))
            display_chat()
            st.stop()
        else:
            st.session_state.chat_history.append((st.session_state.name, user_input))
            reply = kinky_reply(user_input, st.session_state.name)
            st.session_state.chat_history.append(("KINKY BOT", reply))

    display_chat()
