import streamlit as st

st.header('st.button')

if st.button('say hello'):
    st.wite('why hello there')
else:
    st.write('Goodbye')