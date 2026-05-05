import streamlit as st
import pandas as pd
df = pd.read_csv('deputados_2022.csv')

st.markdown("<h1 style='text-align: center;'>Deputados 2022</h1>", unsafe_allow_html=True)
partido = st.selectbox("Escolha um partido", df["partido"].dropna().unique())

df_filtrado = df[df["partido"] == partido]
st.subheader(f"Deputados do partido {partido}")
st.write(df_filtrado)

estado = st.selectbox("Escolha um estado", df["uf"].dropna().unique())
uf = df['uf']

df_filtrado = df[df["uf"] == estado]
st.subheader(f"Deputados do estado {estado}")
st.write(df_filtrado)

