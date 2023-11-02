import streamlit as st
import database

st.set_page_config(layout="wide",page_title="Decision board")
st.subheader("Registre sua decisão")

with st.form(key="Decisao"):
    decisao = st.text_input("Decisão")
    submit_button = st.form_submit_button(label="Registrar")

if submit_button:
    insercao = database.inserir_decisao(decisao)
    if(insercao is not None):
        st.success("Decisão registrada com sucesso!")
    else:
        st.error("Houve um erro na inserção, favor verificar conexão com o banco de dados")