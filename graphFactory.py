import matplotlib.pyplot as plt
import plotly.express as px
from collections import Counter
from nltk.corpus import stopwords
from wordcloud import WordCloud, ImageColorGenerator

def wordCloud(df,column):
    palavras = " ".join(s for s in df[column])
    wordCloud = WordCloud(stopwords=stopwords.words("portuguese"),
                      background_color="black",
                      width=1600, height=800).generate(palavras)  
    return wordCloud
   

def graficoDePalavras(df,column):
    topic_words = [ z.lower() for y in
                       [ x.split() for x in df[column] if isinstance(x, str)]
                       for z in y]
    word_count_dict = dict(Counter(topic_words))
    popular_words = sorted(word_count_dict, key = word_count_dict.get, reverse = True)
    popular_words_nonstop = [w for w in popular_words if w not in stopwords.words("portuguese")]
    plt.bar(range(5), [word_count_dict[w] for w in reversed(popular_words_nonstop[0:5])])
    plt.xticks([x for x in range(5)], reversed(popular_words_nonstop[0:5]))
    plt.title('5 palavras mais frequentes nas reclamações')
    return plt

def graficoDeStatus(count_status):
    return px.pie(values=count_status.values, names=count_status.index,title="<b>Quantidade de reclamações por status</b>",labels={'index':'Status','y':'Quantidade'})

def graficoDeAnos(count_anos):
    return px.bar(count_anos, y=count_anos.values,title="<b>Quantidade de reclamações por ano</b>",labels={'index':'Ano','y':'Quantidade'},text_auto=True)

def graficoDeMeses(count_mes):
    return px.bar(count_mes, y=count_mes.values,title="<b>Quantidade de reclamações por mês</b>",labels={'index':'Mês','y':'Quantidade'},text_auto=True)