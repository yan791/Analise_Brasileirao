import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard do Brasileirão")
st.write("Análise de Times Brasileirão (2003 - 2024)")

dados = pd.read_csv('brasileirao.csv')

opcao = st.selectbox(
    "📊 Escolha qual estatística você quer analisar:",
    ("1. Maiores Campeões", "2. Times com Mais Gols", "3. Times com Mais Vitórias", "4. Media de Gols por Temporada")
)

if opcao == "1. Maiores Campeões":
    df_campeoes = dados[dados['place'] == 1]
    contagem = df_campeoes['team'].value_counts()
    st.bar_chart(contagem)

elif opcao == "2. Times com Mais Gols":
    totalgol = dados.groupby('team')['goals'].sum().sort_values(ascending = False)
    st.bar_chart(totalgol.head(10))

elif opcao == "3. Times com Mais Vitórias":
    maisvit = dados.groupby('team')['won'].sum().sort_values(ascending= False)
    st.bar_chart(maisvit.head(10))