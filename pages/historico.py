import streamlit as st
import database

st.set_page_config(layout="wide",page_title="Decision board")
historico = database.consultar_decisoes()

if (historico is not None):
    if (historico.empty):
        st.write("Nenhuma decisão registrada até o momento")
    else:
        st.table(historico)
else:
    st.error("Houve um erro na consulta do histórico, favor verificar conexão com o banco de dados")