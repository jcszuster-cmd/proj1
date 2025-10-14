import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('deputados_2022 (1).csv')

fig, ax = plt.subplots()
ax.bar(df['Partido'], df['Valor'])
ax.set_xlabel('Partido')
ax.set_ylabel('Valor')
ax.set_title('Gráfico de Barras')

st.pyplot(fig, use_container_width=True)
