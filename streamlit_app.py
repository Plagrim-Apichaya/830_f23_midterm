import streamlit as st
import pandas as pd

st.title("Analysis of Thai agriculture price and the driven factor behind the price dynamic.")
st.header("Thai top agriculture: Rice, Cassava, and Corn")
#st.markdown("this is the header")

page = st.sidebar.radio("Menu",["Home","Rice","Corn","Cassava","Thailand"])
if page == "Home":

    st.image(
                "https://c.tadst.com/gfx/600x337/international-year-plant-health.jpg?1",
                width=400
            )

    st.subheader("This app is to walk you through the analyze of the historical agriculture price data recorded monthly from January 2001 to March 2020")
    st.write("Thailand is a dynamic developing country which is known for its significant contributions to global agriculture exporting. It is a major exporter of agricultural products, with a reputation for delivering their culture along with them  like rice, fruits, cassava, and fish. These agricultural exports not only deliver and serve the nation's economy but also serve as Thai culture and traditions. Additionally, they fulfill the dietary needs of the Thai population. However, the increasing prices of these fundamentals have raised concerns in understanding the intricate dynamics governing their fluctuations.")  

    agri_type = st.multiselect("Agriculture product type", ["Rice", "Corn", "Cassava"])

    url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/TH_agri_price.csv"
    df = pd.read_csv(url, index_col=0)
    st.dataframe(df)
    
    cassava = pd.DataFrame(df.iloc[:,:3])
    corn = pd.DataFrame(df.iloc[:,[0,1,3]])
    rice = pd.DataFrame(df.iloc[:,[0,1,4]])

# "Cassava, Corn, Rice"
    def choose_type(agri_type, year = 2018):
        color = ["#3DB2FF", "#FF2442", "#FFB830"]
        for i in range(len(agri_type)):
            agri = agri_type[i]
            agri_name = agri.columns[-1][:-6]
            select_year_agri = agri[agri["year"] == year]
            
            x = select_year_agri["date"]
            y = select_year_agri.iloc[:,-1]

            plt.figure(figsize=(14, 7))
            plt.scatter(x, y, s = 10, c = color[i])
            plt.plot(x, y, c = color[i], label = agri_name)
            plt.xlabel('Dates', fontsize = 15)
            plt.ylabel('Price (Thai Baht)', fontsize = 15)
            plt.legend(fontsize = 12, loc = 1)
            plt.xticks(rotation = 90)
            st.pyplot()
            
    choose_type([corn, cassava], 2016)

