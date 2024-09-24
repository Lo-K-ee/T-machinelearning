import streamlit as st
import pandas as pd

st.title('🤖Machine learning app')

st.info('This app builds a machine learning model for a simple cleaned dataset')

with st.expander('Raw Cleaned Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/Lo-K-ee/datasets/refs/heads/main/penguins_cleaned.csv')
  df

st.write('*Here, we have displayed both the dependant variable and the independant variables seperately*')
with st.expander('Target and predictors'):
  st.write('**X**')
  X = df.drop('species', axis=1)
  X
  st.write('**y**')
  y = df.species
  y

  # species	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	sex
  
  st.scatter_chart(df, bill_length_mm, body_mass_g)

