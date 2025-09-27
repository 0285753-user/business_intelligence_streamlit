from Modules.Utils.add_df import coffee_data
import streamlit as st
import pandas as pd

def all_data():

  url = 'https://raw.githubusercontent.com/Roby20030202/BI_FINAL_PROJECT/refs/heads/main/filtered_yelp_NJ.csv'

  df = pd.read_csv(url,index_col=0)
  
  df_coffee = coffee_data(df)
  
  # Muestra el DataFrame de forma no editable
  st.subheader('DataFrame No Editable')
  st.dataframe(df_coffee)
