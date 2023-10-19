import streamlit as st
import pandas as pd

st.title("Analysis of Thai agriculture price and the driven factor behind the price dynamic.")
st.header("Thai top agriculture: Rice, Cassava, and Corn")
#st.markdown("this is the header")

st.button("Home")

st.image(
            "https://c.tadst.com/gfx/600x337/international-year-plant-health.jpg?1",
            width=400
        )

st.subheader("This app is to walk you through the analyze of the historical agriculture price data recorded monthly from January 2001 to March 2020")
st.write("Thailand is a dynamic developing country which is known for its significant contributions to global agriculture exporting. It is a major exporter of agricultural products, with a reputation for delivering their culture along with them  like rice, fruits, cassava, and fish. These agricultural exports not only deliver and serve the nation's economy but also serve as Thai culture and traditions. Additionally, they fulfill the dietary needs of the Thai population. However, the increasing prices of these fundamentals have raised concerns in understanding the intricate dynamics governing their fluctuations.")  


#url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/thailand-food-median-prices-2.csv"
url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/Thailand_food_price.csv"
df = pd.read_csv(url, index_col=0)
st.dataframe(df)

