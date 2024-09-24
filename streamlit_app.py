import streamlit as st
import pandas as pd

st.title('🤖Machine learning app')

st.info('This app deploys a machine learning model')

with st.expander('data'):
  df = pd.read_csv('https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv')
  df
