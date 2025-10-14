%pip install streamlit

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('/deputados_2022.csv')

# Calculate the number of candidates per party
party_counts = df['partido'].value_counts().reset_index()
party_counts.columns = ['partido', 'number_of_candidates']

fig, ax = plt.subplots()
ax.bar(party_counts['partido'], party_counts['number_of_candidates'])
ax.set_xlabel('Partido')
ax.set_ylabel('Number of Candidates')
ax.set_title('Number of Candidates per Party')

st.pyplot(fig, use_container_width=True)
