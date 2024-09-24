import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

st.title('🤖Machine learning app')

st.info('This app builds a machine learning model for a simple cleaned dataset')

with st.expander('Raw Cleaned Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/Lo-K-ee/datasets/refs/heads/main/penguins_cleaned.csv')
  df

st.write('*Here, we have displayed both the dependant variable and the independant variables seperately*')
with st.expander('Target and predictors'):
  st.write('**X**')
  X_old = df.drop('species', axis=1)
  X_old
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
  sex = st.radio("Select the sex:",
           ["Male", "Female"], index=None)

  # Inputting a new row in the dataset
  if st.button('Add a new row'):
    new_data = {'island': island,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g,
            'sex': sex}
    input_df = pd.DataFrame(new_data, index=[0])
    st.write(input_df, '*A new row of data has been created*')
    input_penguins = pd.concat([input_df, X_old], axis=0)

st.write('*An input feature based on the selection has been added to the original dataframe*')
with st.expander('Newly modified dependant features'):
  st.write('**X**')
  X = X_old.copy(deep=True)

# Encoding
st.write('Encoded the features "island" & "sex" using labelencoder')
le = LabelEncoder()
with st.expander('Encoded data'):
  X['island'] = le.fit_transform(X['island'])
  X['sex'] = le.fit_transform(X['sex'])
  X
  


    
    
  

