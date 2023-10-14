import pandas as pd
# import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt
from altair import datum
import math
import numpy as np

option = st.selectbox("1","2","3")

st.write('data selected:', option)

url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/thailand-food-median-prices-2.csv"
th_food = pd.read_csv(url)
st.write(" ## dataset")
st.dataframe(th_food)

st.write(" ## descriptive statistic")
th_food_describe = th_food.describe()
st.write(th_food_describe)

afig1 = sns.lmplot(data = th_food, x = th_food["date"], y = th_food["price"], hue = 'category')
st.pyplot(afig1)