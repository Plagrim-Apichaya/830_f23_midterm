import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

# Set the title of the Streamlit app
st.title("My Streamlit App")

# Create a header
st.header("This is a Streamlit App with a Heading")
#st.write(" # Analysis of Thai agriculture price and the driven factor behind the price dynamic.")

url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/thailand-food-median-prices-2.csv"
th_food = pd.read_csv(url)
st.write(" ## dataset")
st.dataframe(th_food)

st.write(" ## descriptive statistic")
th_food_describe = th_food.describe()
st.write(th_food_describe)

afig1 = sns.lmplot(data = th_food, x = th_food["date"], y = th_food["price"], hue = 'category')
st.pyplot(afig1)