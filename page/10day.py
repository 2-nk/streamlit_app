import streamlit as st

st.header("st.selectbox")

option = st.selectbox("What is your favorite color?",
                 ('Blue', 'Red', 'Greenn'))

st.write("Your favorite color is", option)