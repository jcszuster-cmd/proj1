import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('https://ss.cursos.fgv.br/d2l/le/content/179108/viewContent/2436430/View')

plt.bar(df['Categoria'], df['Valor'])
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.title('Gráfico de Barras')
plt.show()

st.matplotlib.pyplot(fig, use_container_width=True, theme="streamlit")
