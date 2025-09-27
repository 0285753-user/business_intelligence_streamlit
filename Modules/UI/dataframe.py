from Modules.Utils.add_df import create_df
import streamlit as st
import pandas as pd

df = create_df()

# Muestra el DataFrame de forma no editable
st.subheader('DataFrame No Editable')
st.dataframe(df)
