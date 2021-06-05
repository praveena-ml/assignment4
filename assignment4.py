#################
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns 

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Data")
#import dataset
df = pd.read_csv('insurance.csv')
insurance = df.head(10)
#Display the table
st.table(insurance)
#############
#bar plot
st.subheader("Bar Plot")
insurance.plot(kind='bar')
st.pyplot()
################

#pairplot
st.subheader("Pairplot")
sns.pairplot(insurance,hue='sex',palette='rainbow')
st.pyplot()

