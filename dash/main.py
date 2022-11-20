import streamlit as st
import requests
from datetime import datetime
from functions import gen_figure

st.set_page_config(page_title="Data Analysis: COVID-19", layout="wide")
all_countries = requests.get("http://127.0.0.1:8000/countries").json()
MIN_DATE = datetime.date(datetime(2020,1,22))
MAX_DATE = datetime.date(datetime(2021,4,10))
min_date = MIN_DATE
max_date = MAX_DATE

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
    min_date = st.sidebar.date_input("Fecha inicial:", min_date, min_value=MIN_DATE, max_value=max_date)
    max_date = st.sidebar.date_input("Fecha final", max_date, min_value=min_date, max_value=MAX_DATE)
    reset = st.sidebar.button('Restaurar')

    if reset:
        min_date = MIN_DATE
        max_date = MAX_DATE
        reset = False
    date_range=(min_date, max_date)

    if countries:
        fig = gen_figure(countries, date_range, chosen_db)
        st.plotly_chart(fig)