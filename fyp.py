import streamlit as st
import pandas as pd


st.header("Data Analytic Final Project")
data=pd.read_csv('winequality-white.csv', sep=';')

st.table(data)


