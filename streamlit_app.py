import streamlit as st
import pandas as pd

st.title("Analysis of Thai agriculture price and the driven factor behind the price dynamic.")
st.header("Thai top agriculture: Rice, Cassava, and ")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
#st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/thailand-food-median-prices-2.csv"
df = pd.read_csv(url, index_col=0)
st.dataframe(df)