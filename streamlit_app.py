import streamlit as st
import time
import pandas as pd

col1, col2, col3 = st.columns([1, 2, 1])

col1.markdown(" # Welcome to my app! ")
col1.markdown(" # Here is some info on the app. ")
col2.markdown(" Thailand Food Price (2014 - 2019) ")

#upload_photo = col2.file_uploader(" Upload a photo", on_change = "chage_photo_state")
input_photo = col2.camera_input(" Take a photo to record your log in today")

url = "https://raw.githubusercontent.com/Plagrim-Apichaya/CMSE830_23/main/thailand-food-median-prices-2.csv?token=GHSAT0AAAAAACH3C2B3L45MDEEGQ7VW6TX4ZIXTBUQ"
th_food = pd.read_csv(url)
st.write(" ## dataset")
st.dataframe(th_food)

st.write(" ## descriptive statistic")
th_food_describe = th_food.describe()
st.write(th_food_describe)

afig1 = sns.lmplot(data = th_food, x = th_food["date"], y = th_food["price"], hue = 'category')
st.pyplot(afig1)