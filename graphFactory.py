import matplotlib.pyplot as plt
import plotly.express as px
from nltk.corpus import stopwords
from wordcloud import WordCloud

def wordCloud(df,column):
    palavras = " ".join(s for s in df[column])
    wordCloud = WordCloud(stopwords=stopwords.words("portuguese"),
                      background_color="black",
                      width=1600, height=800).generate(palavras)  
    return wordCloud
   

def graficoDeStatus(count_status):
    return px.pie(values=count_status.values, names=count_status.index,title="<b>Quantidade de reclamações por status</b>",labels={'index':'Status','y':'Quantidade'})

def graficoDeAnos(count_anos):
    return px.bar(count_anos, y=count_anos.values,title="<b>Quantidade de reclamações por ano</b>",labels={'index':'Ano','y':'Quantidade'},text_auto=True)

def graficoDeMeses(count_mes):
    return px.bar(count_mes, y=count_mes.values,title="<b>Quantidade de reclamações por mês</b>",labels={'index':'Mês','y':'Quantidade'},text_auto=True)