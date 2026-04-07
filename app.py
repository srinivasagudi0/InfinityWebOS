import streamlit as st
import webbrowser as wb
from support import *

st.title("InfinityOS")

if st.button("Youtube"):
    st.write("You clicked the button!")
    wb.open("https://www.youtube.com/")

if st.button("Google"):
    st.write("You clicked the button!")
    wb.open("https://www.google.com/")

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