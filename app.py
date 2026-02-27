import streamlit as st 
import pandas as pd

st.title("Dashboard do Brasileirão (2003 - 2024)")
st.write("Análise de Times Brasileirão")

dados = pd.read_csv('brasileirao.csv')

opcao = st.selectbox(
    "📊 Escolha qual estatística você quer analisar:",
    ("1. Maiores Campeões (1º Lugar)", "2. Times com Mais Gols", "3. Times com Mais Vitórias")
)
if opcao == "1. Maiores Campeões (1º Lugar)":
    df_campeoes = dados[dados['place'] == 1]