# <python_file>.ipynb : notebook 파일
# 동작하는 프로그램으로 만들때는 <python_file>.py
# $ python <python_file>.py

import streamlit as st
def text():
    # markdown
    st.markdown("# mark down")
    st.markdown("**hello world**")
    st.markdown("hi word")

def main():
    st.title("First APP")
    text()

if __name__ == "__main__":
    main()