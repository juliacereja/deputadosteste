import streamlit as st
import pandas as pd
df = pd.read_csv('deputados_2022.csv')

st.markdown("<h1 style='text-align: center;'>Deputados 2022</h1>", unsafe_allow_html=True)
voluntario = st.selectbox("Escolha um partido", df["partido"].dropna().unique())

df_filtrado = df[df["partido"] == partido]
st.subheader(f"Deputados do partido {partido}")
st.write(df_filtrado)

st.metric("Partido", dados["partido"].values[0])
st.metric("Nome civil", dados["nome_civil"].values[0])
st.metric("Cpf", dados["cpf"].values[0])
st.metric("Estado", dados["uf"].values[0])
st.metric("Sexo", dados["sexo"].values[0])
