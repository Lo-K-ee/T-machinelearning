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
  st.write('Data Visualization')
  st.scatter_chart(df, x='bill_length_mm', y='body_mass_g', color='species')

# Data Prep
with st.sidebar:
  st.header('Input Features')
  island = st.radio("Select the Island:",
           ["Torgersen","Dream","Biscoe"], index=None)
  bill_length_mm = st.slider('Bill length (mm)', 32.10, 59.60, 42.51)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.10, 21.50, 17.20)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.00, 231.00, 201.00)
  body_mass_g = st.slider('Body mass (g)', 2700.00, 6300.00, 4207.00)
  gender = st.radio("Select the Gender:",
           ["Male", "Female"], index=None)

  if st.button('Add a new row'):
    new_data = {'island': island,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g,
            'gender': gender}
    input_df = pd.DataFrame(new_data, index=[0])
    st.write(input_df, 'a new row of data has been created')
  input_penguins = pd.concat([input_df, X], axis=0)

with st.expander('Newly modified dependant features'):
  st.write('**X**')
  input_penguins

    
    
    
  

