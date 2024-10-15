import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')
st.header('Proyecto 6')
st.write('Esta aplicación  esta funcional.')

hist_boton = st.button('Contruir histograma')

if hist_boton:
    st.write('Creacion de histograma de los valores del odometro de los autos')
    fig = px.histogram(data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

hist_boton = st.button('Grafico de dispersion')

if hist_boton:
    st.write('Creacion gráfico de dispersión de los valores del odometro de los autos')
    fig = px.scatter(data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

scatter_boton = st.button('Contruir scatter_button ')

if scatter_boton:
    st.write('Creacion de  scatter_button')
    fig = px.scatter(data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
    fig.show()
 

