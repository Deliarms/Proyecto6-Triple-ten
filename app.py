import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

hist_boton = st.button('Contruir histograma')

if hist_boton:
    st.write('Creacion de histograma de los valores del odometro de los autos')
    fig = px.histogram(data, x='odometer')
    st.plotly_chart(fig)
    


 
 
