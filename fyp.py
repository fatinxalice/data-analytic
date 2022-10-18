import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Data Analytic Final Project")
data=pd.read_csv('winequality-white.csv', sep=';')

data.sample(5)

data.describe()

data.columns

data.info()
