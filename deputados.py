import streamlit as st
import pandas as pd
df = pd.read_csv('deputados_2022.csv')

voluntario = st.selectbox("Escolha um voluntário", df["nome"])

dados = df[df["nome"] == voluntario]
st.write(dados)

st.metric("Idade", dados["partido"].values[0])
st.metric("Peso", dados["nome_civil"].values[0])
