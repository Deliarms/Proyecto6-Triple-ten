import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

hist_boton = st.button('Contruir histograma')

if hist_boton:
    st.write('Creacion de histograma de los valores del odometro de los autos')
    fig = px.histogram(data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
    
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') 
fig = px.scatter(car_data, x="odometer", y="price") 
fig.show() 

import streamlit as st

st.header('Lanzar una moneda')

st.write('Esta aplicación  esta funcional.')


 
 
