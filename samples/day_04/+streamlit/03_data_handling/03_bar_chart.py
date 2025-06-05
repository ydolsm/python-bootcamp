import streamlit as st
import pandas as pd

df = pd.read_csv("data/sales/accounts.csv")
st.bar_chart(df, x="year_established", y="revenue")
