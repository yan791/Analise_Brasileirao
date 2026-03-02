import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard do Brasileirão")
st.write("Análise de Times Brasileirão (2003 - 2024)")
dados = pd.read_csv('brasileirao.csv', encoding='latin-1')

opcao = st.selectbox(
    "📊 Escolha qual estatística você quer analisar:",
    ("1. Maiores Campeões", "2. Times com Mais Gols", "3. Times com Mais Vitórias",
      "4. Times com Mais Gols Sofridos", "5. Media de Gols por Temporada")
)

if opcao == "1. Maiores Campeões":
    df_campeoes = dados[dados['place'] == 1]
    contagem = df_campeoes['team'].value_counts()
    st.bar_chart(contagem)

elif opcao == "2. Times com Mais Gols":
    st.subheader('Times com mais gols no Brasileirão')
    gols_time = dados.groupby('team')['goals'].sum().sort_values(ascending = False)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    gols_time.head(10).plot(kind='bar', ax=ax)
    plt.xlabel('')
    plt.xticks(rotation=45)
    plt.ylabel('Quantidade de Gols')
    
    st.pyplot(fig) 

elif opcao == "3. Times com Mais Vitórias":
    maisvit = dados.groupby('team')['won'].sum().sort_values(ascending= False)
    st.bar_chart(maisvit.head(10))

elif opcao == "4. Times com Mais Gols Sofridos":
    sofridos = dados.groupby('team')['goals_taken'].sum().sort_values(ascending = False)
    st.bar_chart(sofridos.head(10))

elif opcao == "5. Media de Gols por Temporada":
    st.subheader('Média de gols por temporada')
    media = dados.groupby('season')['goals'].mean() 
    
    fig, ax = plt.subplots(figsize=(10, 4))
    media.plot(kind='line', ax=ax) 
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de Gols')
    
    st.pyplot(fig) 