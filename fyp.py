import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Data Analytic Final Project")
data=pd.read_csv('winequality-white.csv', sep=';')

st.write(data.sample(5))
st.write(data.describe())
st.write(data.info())

fig, axs = plt.subplots(11, figsize = (10,25))
plt1 = sns.boxplot(data['fixed acidity'], ax = axs[0])
plt2 = sns.boxplot(data['volatile acidity'], ax = axs[1])
plt3 = sns.boxplot(data['citric acid'], ax = axs[2])
plt4 = sns.boxplot(data['residual sugar'], ax = axs[3])
plt5 = sns.boxplot(data['chlorides'], ax = axs[4])
plt6 = sns.boxplot(data['free sulfur dioxide'], ax = axs[5])
plt7 = sns.boxplot(data['total sulfur dioxide'], ax = axs[6])
plt8 = sns.boxplot(data['density'], ax = axs[7])
plt9 = sns.boxplot(data['pH'], ax = axs[8])
plt10 = sns.boxplot(data['sulphates'], ax = axs[9])
plt11 = sns.boxplot(data['alcohol'], ax = axs[10])
plt.tight_layout()

st.pyplot(fig)

data1 = data.drop_duplicates()

bar = sns.countplot(x = data1['quality']).set(title = 'Frequency Chart', 
                                       xlabel = 'Wine Quality', 
                                       ylabel = 'Frequency');

st.pyplot(bar)

sns.heatmap(data1.corr(), annot = True)
plt.gcf().set_size_inches(15, 8)
plt.show()





