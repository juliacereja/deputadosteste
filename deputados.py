import streamlit as st
import pandas as pd
df = pd.read_csv('deputados_2022.csv')

voluntario = st.selectbox("Escolha um voluntário", df["nome"])

dados = df[df["nome"] == voluntario]
