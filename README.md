# ⚽ Análise do Brasileirão (2003 - 2024) 📊

Este é um web dashboard interativo desenvolvido em Python para analisar estatísticas históricas e recentes do Campeonato Brasileiro (Brasileirão). O projeto permite visualizar dados detalhados sobre o desempenho de times e jogadores através de gráficos dinâmicos.

## 🚀 Funcionalidades

O projeto é dividido em páginas para facilitar a navegação e a análise dos dados:

### 👤 Jogadores (Foco em 2024)
- **Top Artilheiros:** Gráfico de barras destacando os jogadores com mais gols.
- **Top Assistências:** Ranking dos maiores garçons do campeonato.
- **Mais Participações em Gols:** Análise combinada de gols e assistências.

### 🛡️ Times (Histórico 2003 - 2024)
- **Maiores Campeões:** Contagem de títulos por equipe.
- **Times com Mais Gols:** Ranking ofensivo histórico.
- **Times com Mais Vitórias:** Equipes que mais venceram partidas no período.
- **Times com Mais Gols Sofridos:** Análise defensiva das equipes.
- **Média de Gols por Temporada:** Gráfico de linha mostrando a evolução da média de gols ao longo dos anos.

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/):** Linguagem principal do projeto.
- **[Streamlit](https://streamlit.io/):** Framework para a criação da interface web interativa.
- **[Pandas](https://pandas.pydata.org/):** Biblioteca para manipulação, limpeza e agrupamento dos dados.
- **[Plotly Express](https://plotly.com/python/plotly-express/):** Criação dos gráficos interativos e estilizados.

## 📁 Estrutura do Projeto

```text
├── data/
│   ├── brasileirao.csv       # Base de dados histórica dos times
│   ├── database.csv          # Base de dados estatística dos jogadores
│   └── teams.csv             # Informações complementares das equipes
├── pages/
│   ├── jogadores.py          # Página de análise individual de jogadores
│   └── times.py              # Página de análise histórica dos clubes
├── dashboard.py              # Arquivo principal de execução do Streamlit
└── README.md
