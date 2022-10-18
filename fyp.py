import streamlit as st
import pandas as pd


st.header("Data Analytic Final Project")
data=pd.read_csv('winequality-white.csv', sep=';')

st.write(data.describe())
st.write(data.shape)


