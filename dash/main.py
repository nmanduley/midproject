import streamlit as st
import requests
from datetime import datetime
from functions import gen_figure
# import matplotlib.pyplot as plt
# import plotly.graph_objs as go
# import plotly.express as px
# import pandas as pd

st.set_page_config(page_title="Data Analysis: COVID-19", layout="wide")
all_countries = requests.get("http://127.0.0.1:8000/countries").json()
MIN_DATE = datetime.date(datetime(2020,1,22))
MAX_DATE = datetime.date(datetime(2021,4,10))

# Header
with st.container():
    st.subheader("Proyecto de mitad de bootcamp BDML")
    st.title("Data Analysis: COVID-19")
    st.write("Nicolas Manduley")

# Body
with st.container():
    st.write('---')
    st.header("Consultar/comparar casos confirmados, numero de muertes o recuperados por pais")
    # Sidebar
    st.sidebar.title("Menu")
    chosen_db = st.sidebar.radio('Seleccionar base de datos:', \
        options=['Casos confirmados', 'Muertes', 'Recuperados'])
    countries = st.sidebar.multiselect("Selecciona uno o varios paises:", [c["Country/Region"] for c in all_countries])
    date_range = st.sidebar.slider("Selecciona rango de fechas:", value=[MIN_DATE, MAX_DATE])

    if countries:
        fig = gen_figure(countries, date_range, chosen_db)
        st.plotly_chart(fig)