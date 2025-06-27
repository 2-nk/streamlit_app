import streamlit as st

st.header('st.latex')

st.latex(r'''
         a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} =
         \sum_{k=0}^{n-1} ar^k =
         a\left(\frac{1-r^{m}}{1-r}\right)
         ''')