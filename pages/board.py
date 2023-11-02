import streamlit as st
import pandas as pd
import configDate
import database
import graphFactory

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide",page_title="Decision board")
reclamacoes = database.carregar_dataframe()

with st.sidebar:
    st.subheader('Filtros')
    filtro_empresa = st.selectbox(
        "Selecione a empresa:",
        options=reclamacoes['empresa'].unique()
        )
    filtro_local = st.selectbox(
        "Selecione o local:",
        options=reclamacoes['local'].unique()
        ) 
    filtro_palavra_chave = st.text_input('Pesquisar por palavra chave')
    
    
    reclamacoes_filtradas = reclamacoes.query('empresa == @filtro_empresa & local == @filtro_local')
    reclamacoes_filtradas = reclamacoes_filtradas[reclamacoes_filtradas.texto.str.contains(filtro_palavra_chave)]

    count_status = reclamacoes_filtradas['status'].value_counts()
    fig_status = graphFactory.graficoDeStatus(count_status)


    count_anos = pd.to_datetime(reclamacoes_filtradas['datahora']).dt.year.value_counts()
    fig_anos = graphFactory.graficoDeAnos(count_anos)

    count_mes = pd.to_datetime(reclamacoes_filtradas['datahora']).dt.month.apply(lambda x: configDate.MESES[x-1]).value_counts()
    fig_meses = graphFactory.graficoDeMeses(count_mes)
    
    #fig_palavras = graphFactory.graficoDePalavras(reclamacoes_filtradas, 'texto')
    
    wordcloud_reclamacoes = graphFactory.wordCloud(reclamacoes_filtradas, 'texto')
    figrec, axrec = graphFactory.plt.subplots(figsize=(10,6))
    axrec.imshow(wordcloud_reclamacoes, interpolation='bilinear')
    axrec.set_axis_off()
    graphFactory.plt.title('Palavras mais frequentes das reclamações')
    fig_reclamacoes = graphFactory.plt.imshow(wordcloud_reclamacoes)
    
    wordcloud_respostas = graphFactory.wordCloud(reclamacoes_filtradas, 'resposta')
    figres, axres = graphFactory.plt.subplots(figsize=(10,6))
    axres.imshow(wordcloud_respostas, interpolation='bilinear')
    axres.set_axis_off()
    graphFactory.plt.title('Palavras mais frequentes das respostas')
    fig_respostas =  graphFactory.plt.imshow(wordcloud_respostas)

st.plotly_chart(fig_status)
st.plotly_chart(fig_anos)
st.plotly_chart(fig_meses)
st.pyplot(fig_reclamacoes.figure)
st.pyplot(fig_respostas.figure)