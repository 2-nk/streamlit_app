import streamlit as st
import pandas as pd

st.title("st.file_uploader")

st.subheader("Input CSV")

uploaded_file = st.file_uploader("Browse files")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
else:
    st.info("☝️ Upload a CSV file")        