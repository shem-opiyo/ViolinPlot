st.write("## shem nicholas opiyo")
st.write("## SCT211-0509/2021")
st.write("##scientific computing assignment 4")
import matplotlib.pyplot as plt
import seaborn as sns   
import pandas as pd
import streamlit as st

st.write("## Original dataset in the spreadsheet file")
countries = pd.read_csv("D:/course work/2.2/2023 edition/ICS 2207 scientific computing/ICS 2207 scientific computing assignments/HW3/excelFile.csv")
st.write(countries.head())

st.write("## filtered data that focuses on 2007")
countries = countries[countries["year"] == 2007]
st.write(countries.head())

st.write("## The violin plot")
sns.violinplot(x = countries["pop"], y = countries["lifeExp"], hue = countries["gdpPercap"])
plt.show()
st.pyplot()
