import streamlit as st
import plotly.graph_objs as go
# import plotly.express as px 
import requests
import pandas as pd
import json

st.set_page_config(page_title="Data Analysis: COVID-19", layout="wide")

all_countries = requests.get("http://127.0.0.1:8000/countries").json()

# Header
with st.container():
    st.subheader("Proyecto de mitad de bootcamp BDML")
    st.title("Data Analysis: COVID-19")
    st.write("Nicolas Manduley")

# Body
with st.container():
    st.write('---')
    st.header("Primera seccion")
    st.write("Test con un pais (para casos confirmados)")

    country = st.multiselect("Select a country", [c["Country/Region"] for c in all_countries])

    test = requests.get("http://127.0.0.1:8000/confirmed/{country}").json()
    st.text(test)
    # df = pd.DataFrame(test)
    # fig = go.Figure(
    #     data = [go.Scatter(df[])]
    # )


    # st.plotly_chart(graph)

    # dates = test.keys()
    # cases = test.values()

