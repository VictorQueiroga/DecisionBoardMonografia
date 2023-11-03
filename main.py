import streamlit as st
from PIL import Image

st.set_page_config(layout="wide",page_title="Decision board")

def main():
    with st.sidebar:
        st.title("Decision Board")
        logo = Image.open('decision_board.jpg')
        st.image(logo, use_column_width=True)
    st.write("Boas vindas ao Decision Board")

if __name__ == '__main__':
    main()