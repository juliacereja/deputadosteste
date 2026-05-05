import panda as pd
df = pd.read_csv('deputados_2022.csv')

voluntario = st.selectbox("Escolha um voluntário", df["Nome"])
