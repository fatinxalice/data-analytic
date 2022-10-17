import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('https://docs.google.com/spreadsheets/d/1StLk2E1fqcHRUS-NxYM98UEFY0kdynUDXbamn_z3DyI/edit?usp=sharing', sep=';')

data.sample(5)