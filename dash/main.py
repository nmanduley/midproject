import streamlit as st
import requests
import json

st.set_page_config(page_title="Data Analysis: COVID-19", layout="wide")

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

    country = "Spain"

    req = requests.get("http://127.0.0.1:8000/confirmed/{country}")
    test = json.load(req)
    dates = test.keys()
    cases = test.values()
    print(dates)

