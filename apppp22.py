import random
import streamlit as st
from textblob import TextBlob

def flirty_reply(text, name):
    text_lower = text.lower()
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 (negative) to +1 (positive)

    # Playful keyword triggers
    teasing = ["naughty", "flirt", "kiss", "love", "date", "romantic"]
    compliments = ["cute", "beautiful", "handsome", "smart", "pretty", "amazing"]
    greetings = ["hi", "hello", "hey", "yo"]

    if any(word in text_lower for word in compliments):
        responses = [
            f"Aww, {name}, now you’re making me blush ☺️",
            f"Stop it, {name}, I might get used to your compliments 😉",
            f"You always know how to make me smile, {name} 💕",
        ]
    elif any(word in text_lower for word in teasing):
        responses = [
            f"Oh wow, {name}… you’re bold 😏",
            f"Careful, {name}, I might start playing along 😄",
            f"You’re definitely keeping this spicy, {name} 🔥",
        ]
    elif any(word in text_lower for word in greetings):
        responses = [
            f"Hey {name}! I was hoping you’d come 💖",
            f"Hello, {name} 🌟 What mischief are we up to today?",
            f"Hi {name}, I already missed you 😍",
        ]
    else:
        if sentiment > 0.3:  # Positive
            responses = [
                f"I love your energy, {name} ✨",
                f"That’s so sweet of you, {name} 💕",
                f"You always brighten the conversation, {name} 😍",
            ]
        elif sentiment < -0.2:  # Negative
            responses = [
                f"Aww, cheer up {name}, I’m here for you 💖",
                f"Don’t be sad, {name}, I’ll make you smile 😘",
                f"Even on tough days, I like chatting with you, {name} 🌸",
            ]
        else:  # Neutral / unsure
            responses = [
                f"Hmm interesting… tell me more, {name} 😉",
                f"I like where this is going, {name} 😏",
                f"You make even normal chats fun, {name}!",
            ]

    return random.choice(responses)

# Streamlit UI
st.set_page_config(page_title="Flirty Chatbot", page_icon="💖")

st.title("💖 Flirty Chatbot 💖")
st.markdown("Enter your name to start chatting.")

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
                st.markdown(f"**{st.session_state.name}:** {message}")
            else:
                st.markdown(f"<span style='color:deeppink'>*Flirty Bot:* {message}</span>", unsafe_allow_html=True)

    user_input = st.text_input(f"{st.session_state.name}:", key="input")

    if user_input:
        if user_input.lower() == "exit":
            st.session_state.chat_history.append(("Flirty Bot", f"See you soon, {st.session_state.name} 💕 Can’t wait to chat again!"))
            display_chat()
            st.stop()
        else:
            st.session_state.chat_history.append((st.session_state.name, user_input))
            reply = flirty_reply(user_input, st.session_state.name)
            st.session_state.chat_history.append(("Flirty Bot", reply))

    display_chat()
