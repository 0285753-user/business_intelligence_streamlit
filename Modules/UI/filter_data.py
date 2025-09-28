from Modules.Utils.filter_df import filtered_data
import streamlit as st
import pandas as pd

def clean_data():

  url = 'https://raw.githubusercontent.com/Roby20030202/BI_FINAL_PROJECT/refs/heads/main/filtered_yelp_NJ.csv'

  df = pd.read_csv(url,index_col=0)
  
  clean_coffee = filtered_data(df)
  
  # Muestra el DataFrame de forma no editable
  st.subheader('Set Original de Datos')
  st.dataframe(clean_coffee, width=1500)
