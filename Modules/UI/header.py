#Encabezado de la interfaz grafica de la app

import streamlit as st

def show_header(text_title: str):
  #layout: logo + title side by side
  col1, col2 = st.columns([1, 6])

  with col1:
    st.image("./coffee.jpg", width=200)
  
  with col2:
    st.title(text_title)
    st.caption("Developed for: *Business Inteligene Project*")
    st.caption("Developed by Team 4")
