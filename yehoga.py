import streamlit as st
import streamlit.components.v1 as components

# Load your HTML
html_code = open("reload.html", "r", encoding="utf-8").read()

# Streamlit title
st.set_page_config(page_title="Momma's Form", layout="centered")
st.title("💖 Momma’s Form 💖")

# Display HTML content
components.html(html_code, height=1000, scrolling=True)
