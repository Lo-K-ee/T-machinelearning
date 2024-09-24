import streamlit as st
import pandas as pd

st.title('🤖Machine learning app')

st.info('This app deploys a linear regression model for a simple cleaned dataset')

with st.expander('data'):
  df = pd.read_csv('https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv')
  df
