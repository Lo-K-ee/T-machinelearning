import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


st.title('🤖Machine learning app')

st.info('This app builds a ML model and predicts the output for an input feature from the user')

with st.expander('Raw Cleaned Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/Lo-K-ee/datasets/refs/heads/main/penguins_cleaned.csv')
  df

st.write('*Here, we have displayed both the dependant variable and the independant variables seperately*')
with st.expander('Target and predictors'):
  st.write('**X**')
  X = df.drop('species', axis=1)
  X_new = df.drop('species', axis=1)
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
    X_new = pd.concat([input_df, X], axis=0)

st.write('*An input feature based on the selection has been added to the original dataframe*')
with st.expander('Newly modified dependant features'):
  st.write('**X_new**')
  X_new

# Encoding
st.write('Encoded the features "island" & "sex" using labelencoder')
le = LabelEncoder()
with st.expander('Encoded data'):
  st.write('**X**')
  X['island'] = le.fit_transform(X['island'])
  X['sex'] = le.fit_transform(X['sex'])
  X
  st.write('**X_new**')
  X_new['island'] = le.fit_transform(X_new['island'])
  X_new['sex'] = le.fit_transform(X_new['sex'])
  X_new
  st.write('**y**')
  y = le.fit_transform(y)
  y

# Model Training 
st.write("Now we're gonna train Random forest classifier for this problem")
with st.expander('Model Training'):
  rfc = RandomForestClassifier()
  rfc.fit(X, y)
  # Making predictions using the trained model
  pred = rfc.predict(X_new[:1])
  pred_prob = rfc.predict_proba(X_new[:1])
  # Converting the Numpy array into a df to give appropriate column names
  pred_prob_df=pd.DataFrame(pred_prob)
  pred_prob_df.columns = ['Adelie', 'Gentoo', 'Chinstrap']
  pred_prob_df
  # Predicted value
  penguin_species = np.array(['Adelie', 'Gentoo', 'Chinstrap'])
  st.write('The predicted penguin for the input feature is')
  st.success(str(penguin_species[pred][0]))
  
  


    
    
  

