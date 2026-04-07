import streamlit as st
import webbrowser as wb
import shlex

st.title("InfinityOS")



if st.button("Youtube"):
    st.write("You clicked the button!")
    wb.open("https://www.youtube.com/")

if st.button("Google"):
    st.write("You clicked the button!")
    wb.open("https://www.google.com/")

if st.button("Caluculator"):
    # working on this and I should focus on it opening in both windows and mac

