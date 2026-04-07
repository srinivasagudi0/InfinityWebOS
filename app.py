import streamlit as st
import webbrowser as wb
from support import *

st.title("InfinityOS")
st.set_page_config(page_title="InfinityOS", page_icon=":computer:", layout="wide")

# Custom CSS for a floating button at the bottom right for Youtube.
st.markdown("""
    <style>
    .floating-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 9999;
        background-color: #ff4b4b;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 16px 32px;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Create a floating button using HTML for YouTube.
st.markdown('''
    <form action="https://www.youtube.com/" target="_blank">
        <button class="floating-btn" type="submit">Youtube</button>
    </form>
''', unsafe_allow_html=True)

# Custom CSS for a floating button at the bottom left for Google.
st.markdown("""
    <style>
    .floating-btn-left {
        position: fixed;
        bottom: 30px;
        left: 30px;
        z-index: 9999;
        background-color: #4b79ff;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 16px 32px;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <form action="https://www.google.com/" target="_blank">
        <button class="floating-btn-left" type="submit">Google</button>
    </form>
""", unsafe_allow_html=True)

if st.button("Calculator"):
    st.write("You clicked the button!")
    open_calculator()

if st.button("Notepad"):
    st.write("You clicked the button!")
    open_notepad()

if st.button("File Explorer"):
    st.write("You clicked the button!")
    open_file_explorer()

if st.button("Settings"):
    st.write("You clicked the button!")
    open_settings()

if st.button("Music Player"):
    st.write("You clicked the button!")
    open_music_player()