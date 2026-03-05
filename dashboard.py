import streamlit as st

st.set_page_config(
    page_title="Dashboard do Brasileirão", 
    page_icon="⚽", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚽ Dashboard do Brasileirão")
st.markdown("### Bem-vindo ao portal de estatísticas do campeonato mais disputado do mundo!")
st.divider()
st.info("👈 **Dica de Navegação:** Utilize o menu lateral esquerdo para explorar as seções de **Times** ou **Jogadores**.")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    #### O que você vai encontrar aqui:
    * 🏆 **Classificação e Desempenho:** Acompanhe a evolução do seu time do coração.
    * 👟 **Estatísticas de Jogadores:** Gols, assistências, cartões e muito mais.
    * 📈 **Gráficos Interativos:** Analise os dados de forma visual e intuitiva.
    """)

with col2:
    st.success("Todos os dados de 2003 a 2024! 🟢")