import streamlit as st
import pandas as pd

df = pd.read_csv("data/sales/accounts.csv")
st.scatter_chart(df, x="revenue", y="employees", color="sector")
