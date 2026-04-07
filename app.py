import streamlit as st
import webbrowser as wb
from support import open_calculator

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
