import streamlit as st
import pandas as pd
import mysql.connector as connection
import configDatabase
from datetime import datetime


def abrir_conexao():
    db = connection.connect(host=configDatabase.HOST,database=configDatabase.DATABASE,user=configDatabase.USER, passwd=configDatabase.PASSWORD,use_pure=True)
    return db

@st.cache_data
def carregar_dataframe():
    result_dataFrame = None
    try:
        mydb = abrir_conexao()
        query = "Select * from reclamacao;"
        result_dataFrame = pd.read_sql(query,mydb)
        mydb.close()
    except Exception as e:
        mydb.close()
        print(str(e))
    finally:
        return result_dataFrame


def consultar_decisoes():
    result_dataFrame = None
    try:
        mydb = abrir_conexao()
        query = "Select decisao, dataregistro from decisao order by dataregistro desc;"
        result_dataFrame = pd.read_sql(query,mydb)
        mydb.close()
    except Exception as e:
        mydb.close()
        print(str(e))
    finally:
        return result_dataFrame

def inserir_decisao(decisao):
    rowcount = None
    try:
        mydb = abrir_conexao()
        cursor = mydb.cursor()
        data_atual = datetime.now()
        query = ("INSERT INTO decisao (decisao,dataregistro) VALUES (%s,%s)")
        dados_decisao = (decisao,data_atual)
        cursor.execute(query,dados_decisao)
        mydb.commit()
        rowcount = cursor.rowcount
        cursor.close()
        mydb.close()
    except Exception as e:
        cursor.close()
        mydb.close()
        print(str(e))
    finally:
        return rowcount