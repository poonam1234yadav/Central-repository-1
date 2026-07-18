import streamlit as st

st.title("My First Streamlit App")
name = st.text_input("Enter your name")
if st.button("Submit"):
    st.success(f"Hello, {name}!")
st.write("Welcome to Streamlit!")
st.write("This is my first app.")
st.write("Learning Python is fun!")
