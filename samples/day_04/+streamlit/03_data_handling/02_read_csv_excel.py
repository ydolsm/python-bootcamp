import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("File:", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    st.write(f"Uploaded file: {uploaded_file.name}")

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith((".xlsx", ".xls")):
        df = pd.read_excel(uploaded_file)

    st.write(df)
