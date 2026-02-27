import streamlit as st 
import pandas as pd

st.title("Dashboard do Brasileirão")
st.write("Análise de Times Brasileirão (2003 - 2024)")

dados = pd.read_csv('brasileirao.csv')

opcao = st.selectbox(
    "📊 Escolha qual estatística você quer analisar:",
    ("1. Maiores Campeões (1º Lugar)", "2. Times com Mais Gols", "3. Times com Mais Vitórias")
)
if opcao == "1. Maiores Campeões (1º Lugar)":
    df_campeoes = dados[dados['place'] == 1]
    contagem = df_campeoes['team'].value_counts()
    st.bar_chart(contagem)