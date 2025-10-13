import pandas as pd
import streamlçit as st

dataset = pd.read_csv ('https://www.irdx.com.br/media/uploads/paises.csv')

st.dataframe(dataset)
