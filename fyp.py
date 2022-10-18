import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Data Analytic Final Project")
data=pd.read_csv('winequality-white.csv', sep=';')

st.write(data.sample(5))
st.write(data.describe())
st.write(data.info())

fig, axs = plt.subplots(11, figsize = (10,15))
plt1 = sns.boxplot(data['fixed acidity'], ax = axs[0])
plt2 = sns.boxplot(data['volatile acidity'], ax = axs[1])
plt3 = sns.boxplot(data['citric acid'], ax = axs[2])
plt.tight_layout()

st.write(plt1)
st.write(plt2)
st.write(plt3)





