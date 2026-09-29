import streamlit as st

st.title("My First Streamlit Cloud App")

st.write("Hello Students!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success("Welcome " + name)