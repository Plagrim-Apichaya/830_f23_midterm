#pip install streamlit pandas numpy matplotlib seaborn plotly

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset from the provided URL
url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/thailand-food-median-prices-2.csv"
df = pd.read_csv(url)

# Set the title of your Streamlit app
st.title("Thai Agriculture Price Analysis")

# Display a sample of the dataset
st.subheader("Sample of the Dataset")
st.write(df.head())

# Basic statistics and insights
st.subheader("Basic Statistics and Insights")
st.write(df.describe())

# Visualize price dynamics over time
st.subheader("Price Dynamics Over Time")
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Year", y="Median_Price", hue="Product", ax=ax)
st.pyplot(fig)

# Analyze factors driving price dynamics (You can replace this with your analysis)
st.subheader("Factors Driving Price Dynamics")

# Filter data for specific products or regions for analysis
selected_product = st.selectbox("Select a Product for Analysis", df['Product'].unique())
filtered_data = df[df['Product'] == selected_product]

# Create scatter plot to explore relationships
fig = px.scatter(filtered_data, x="Rainfall_mm", y="Median_Price",
                 title=f"Relationship Between Rainfall and Median Price for {selected_product}",
                 labels={"Rainfall_mm": "Rainfall (mm)", "Median_Price": "Median Price"})
st.plotly_chart(fig)

# Add more analysis as needed

# You can continue to add more Streamlit components for further analysis, visualizations, and insights.

# Save and share your analysis
st.subheader("Conclusion")
st.write("This is your analysis conclusion.")

# To run this Streamlit app, open your terminal and navigate to the directory containing the script, then run:
# streamlit run your_script_name.py

"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
"""