import streamlit as st

st.header('st.multiselect')

option = st.multiselect(
    "What are your favorite colors",
    ['Yellow', 'Red', 'Green', 'Blue'],
    ['Yellow', 'Red'])

st.write("You selected:", option)