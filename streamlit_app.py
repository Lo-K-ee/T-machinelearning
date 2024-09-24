import streamlit as st
import pandas as pd

st.title('🤖Machine learning app')

st.info('This app deploys a linear regression model for a simple cleaned dataset')

with st.expander('Raw Cleaned Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/Lo-K-ee/datasets/refs/heads/main/penguins_cleaned.csv')
  df

st.write('*Here, we have displayed both the dependant variable and the independant variables seperately*')
with st.expander('Target and predictors'):
  st.write('**X**')
  X = df.drop('species')
  X
  st.write('**y**')
  y = df.species
  y
  


