import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import altair as alt
# import altair_viewer


st.title("Analysis of Thai agriculture price and the driven factor behind the price dynamic.")
st.header("Thai top agriculture: Rice, Corn, and Cassava")
st.write("Project by: Apichaya Thaneerat (MSU)")
#st.markdown("this is the header")

url = "https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/TH_agri_price.csv"
df = pd.read_csv(url, index_col=0)
descriptive = df.describe()
    
cassava = pd.DataFrame(df.iloc[:,:3])
corn = pd.DataFrame(df.iloc[:,[0,1,3]])
rice = pd.DataFrame(df.iloc[:,[0,1,4]])

#####--------------- RICE ---------------####
rice_area = pd.read_csv("https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/rice.csv",
                        thousands=',')
    
select_rice_area = rice_area[rice_area["year"] >= 2014]
selected_rice_area = select_rice_area[select_rice_area["year"] <= 2019]
selected_rice_area = selected_rice_area.reset_index()

rice_mean = rice.groupby('year')['rice_price'].mean().reset_index()
rice_mean["Rice Area (1000 Ha)"] = selected_rice_area["Area (1000Ha)"]
rice_mean["Rice Production (1000 Tons)"] = selected_rice_area["Production (1000 Tons)"]
rice_mean["Rice Yield (T/Ha)"] = selected_rice_area["Yield (T/Ha)"]

#####--------------- CORN ---------------####
corn_area = pd.read_csv("https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/corn.csv",
                       thousands=',')
select_corn_area = corn_area[corn_area["year"] >= 2014]
selected_corn_area = select_corn_area[select_corn_area["year"] <= 2019]
selected_corn_area = selected_corn_area.reset_index()
corn_mean = corn.groupby('year')['corn_price'].mean().reset_index()
corn_mean["Corn Area (1000 Ha)"] = selected_corn_area["Area (1000Ha)"]
corn_mean["Corn Production (1000 Tons)"] = selected_corn_area["Production (1000 Tons)"]
corn_mean["Corn Yield (T/Ha)"] = selected_corn_area["Yield (T/Ha)"]

#####--------------- CASSAVA ---------------####
cassava_mean = cassava.groupby('year')['cassava_price'].mean().reset_index()

#####--------------- climate ---------------####
th_temp = pd.read_csv("https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/TH_mean_temperature.csv")
th_precip = pd.read_csv("https://raw.githubusercontent.com/Plagrim-Apichaya/830_f23_midterm/main/TH_precipitation.csv")

th_temp_select = th_temp[(th_temp["year"] >= 2014) & (th_temp["year"] <= 2019)].reset_index()
th_precip_select = th_precip[(th_precip["year"] >= 2014) & (th_precip["year"] <= 2019)].reset_index()

corn_mean["Precipitation"] = th_precip_select["precipitation"]
corn_mean["Mean Surface Temperature"] = th_temp_select["mean surface temperature"]

rice_mean["Precipitation"] = th_precip_select["precipitation"]
rice_mean["Mean Surface Temperature"] = th_temp_select["mean surface temperature"]

cassava_mean["Precipitation"] = th_precip_select["precipitation"]
cassava_mean["Mean Surface Temperature"] = th_temp_select["mean surface temperature"]

# agri_type = ["Rice", "Corn", "Cassava"]
def str_to_MainDF(agri_type):
    if agri_type == "Corn":
        agri_type_df = corn
        color = "orange"
    elif agri_type == "Rice":
        agri_type_df = rice
        color = "greenyellow"
    elif agri_type == "Cassava":
        agri_type_df = cassava
        color = "deepskyblue"
    return agri_type_df, color

def detail_plot(agri_type, year = 2018):
    agri_type_df, color = str_to_MainDF(agri_type)
    select_year = agri_type_df[agri_type_df["year"] == year]
    chart_1 = alt.Chart(select_year).mark_line(color = color).encode(
        x = alt.X('date', title = 'Dates'),
        y = alt.Y(select_year.columns[-1], title = 'Price (Thai Baht)'),
        tooltip=['date', select_year.columns[-1]],
        strokeWidth = alt.value(4)
    ).properties(
        width = 600,
        height = 300,
    )
    
    chart_2 = alt.Chart(select_year).mark_point(color = "tomato", size = 150).encode(
        x = alt.X('date', title = 'Dates'),
        y = alt.Y(select_year.columns[-1], title = 'Price (Thai Baht)'),
        tooltip=['date', select_year.columns[-1]]
    )
    
    chart = chart_1 + chart_2
    return chart

#option = ["Price", "Area", "Production"]
def line_plot(option):
    if option == "Price":
        print("price")
        #------------------- a ----------------
        chart_a = alt.Chart(corn_mean).mark_line().encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('corn_price:Q', title = "Corn Price"),
            color = alt.value('orange'),
            tooltip = ['year', 'corn_price']
        ).properties(
            width = 150,
            height = 300,
            title = 'Corn'
        )
        point_a = alt.Chart(corn_mean).mark_point(color = 'tomato', size = 100).encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('corn_price:Q', title = "Corn Price")
        )
        a_plot = chart_a + point_a
        
        #------------------- b ----------------
        chart_b = alt.Chart(rice_mean).mark_line().encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('rice_price:Q', title = "Rice Price"),
            color = alt.value('greenyellow'),
            tooltip = ['year', 'rice_price']
        ).properties(
            width = 150,
            height = 300,
            title = 'Rice'
        )
        point_b = alt.Chart(rice_mean).mark_point(color = 'tomato', size = 100).encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('rice_price:Q', title = "Rice Price")
        )
        b_plot = chart_b + point_b
        
        #------------------- c ----------------
        chart_c = alt.Chart(cassava_mean).mark_line().encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('cassava_price:Q', title = "Cassava Price"),
            color = alt.value('deepskyblue'),
            tooltip = ['year', 'cassava_price']
        ).properties(
            width = 150,
            height = 300,
            title = 'Cassava'
        )
        point_c = alt.Chart(cassava_mean).mark_point(color = 'tomato', size = 100).encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('cassava_price:Q', title = "Cassava Price")
        )
        c_plot = chart_c + point_c

        combined_chart = alt.hconcat(a_plot, b_plot, c_plot).resolve_scale(y = 'shared')
        
    elif option == "Area":
        #------------------- a ----------------
        chart_a = alt.Chart(corn_mean).mark_line().encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Corn Area (1000 Ha):Q', title = "Corn Area (1000 Ha)"),
            color = alt.value('orange'),
            tooltip = ['year', 'Corn Area (1000 Ha)']
        ).properties(
            width = 150,
            height = 300,
            title = 'Corn'
        )
        point_a = alt.Chart(corn_mean).mark_point(color = 'tomato', size = 100).encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Corn Area (1000 Ha):Q', title = "Corn Area (1000 Ha)")
        )
        a_plot = chart_a + point_a

        #------------------- b ----------------
        chart_b = alt.Chart(rice_mean).mark_line().encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Rice Area (1000 Ha):Q', title = "Rice Area (1000 Ha)"),
            color = alt.value('greenyellow'),
            tooltip = ['year', 'Rice Area (1000 Ha)']
        ).properties(
            width = 150,
            height = 300,
            title = 'Rice'
        )
        point_b = alt.Chart(rice_mean).mark_point(color = 'tomato', size = 100).encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Rice Area (1000 Ha):Q', title = "Rice Area (1000 Ha)")
        )
        b_plot = chart_b + point_b
        
        combined_chart = alt.hconcat(a_plot, b_plot).resolve_scale(y = 'shared')
        
    elif option == "Production":
        #------------------- a ----------------
        chart_a = alt.Chart(corn_mean).mark_line().encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Corn Production (1000 Tons):Q', title = "Corn Production (1000 Tons)"),
            color = alt.value('orange'),
            tooltip = ['year', 'Corn Production (1000 Tons)']
        ).properties(
            width = 150,
            height = 300,
            title = 'Corn'
        )
        point_a = alt.Chart(corn_mean).mark_point(color = 'tomato', size = 100).encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Corn Production (1000 Tons):Q', title = "Corn Production (1000 Tons)")
        )
        a_plot = chart_a + point_a

        #------------------- b ----------------
        chart_b = alt.Chart(rice_mean).mark_line().encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Rice Production (1000 Tons):Q', title = "Rice Production (1000 Tons)"),
            color = alt.value('greenyellow'),
            tooltip = ['year', 'Rice Production (1000 Tons)']
        ).properties(
            width = 150,
            height = 300,
            title = 'Rice'
        )
        point_b = alt.Chart(rice_mean).mark_point(color = 'tomato', size = 100).encode(
            x = alt.X('year', title = "Year"),
            y = alt.Y('Rice Production (1000 Tons):Q', title = "Rice Production (1000 Tons)")
        )
        b_plot = chart_b + point_b
        
        combined_chart = alt.hconcat(a_plot, b_plot).resolve_scale(y = 'shared')
    return combined_chart

def heatmap(option):
    cor_data = (option.corr().stack()
                  .reset_index()     # The stacking results in an index on the correlation values, we need the index as normal columns for Altair
                  .rename(columns={0: 'correlation', 'level_0': 'variable1', 'level_1': 'variable2'}))
    cor_data['correlation_label'] = cor_data['correlation'].map('{:.2f}'.format)  # Round to 2 decimal

    base = alt.Chart(cor_data).encode(
        x = 'variable2:O',
        y = 'variable1:O'    
    )

    text = base.mark_text().encode(
        text = 'correlation_label',
        color = alt.condition(
            alt.datum.correlation > 0.5, 
            alt.value('white'),
            alt.value('black')
        ), tooltip=['variable2', 'variable1', 'correlation']
    )

    # The correlation heatmap
    cor_plot = base.mark_rect().encode(
        alt.Color('correlation:Q', scale = alt.Scale(scheme = 'redblue'),
                 ),
        tooltip = ['variable2', 'variable1', 'correlation']
    )

    larger_figure = (cor_plot + text).properties(
        width = 600,
        height = 600
    )

    return larger_figure

def precip_plot(agri_type):
    bin_width = 0.5
    chart_1 = alt.Chart(corn_mean).mark_bar(color = "lightskyblue").encode(
        x = alt.X('year:O', bin = alt.Bin(step = bin_width), title = 'Year'),
        y = 'Precipitation',
        tooltip = ['year', 'Precipitation']
    ).properties(
        width = 400,
        height = 400
    )

    chart_2 = alt.Chart(corn_mean).mark_line(color = "royalblue").encode(
        x = alt.X('year:O', bin = alt.Bin(step = bin_width), title = 'Year'),
        y = alt.Y('Mean Surface Temperature', scale = alt.Scale(domain = [25, 30])),
        tooltip = ['year', 'Mean Surface Temperature'],
        strokeWidth = alt.value(3)
    ).properties(
        width = 400,
        height = 400
    )

    chart_3 = alt.Chart(corn_mean).mark_point(filled = False, color = "tomato", size = 100).encode(
        x = alt.X('year:O', bin = alt.Bin(step = bin_width), title = 'Year'),
        y = alt.Y('Mean Surface Temperature', scale = alt.Scale(domain = [25, 30])),
        tooltip = ['year', 'Mean Surface Temperature']
    ).properties(
        width = 400,
        height = 400
    )

    dual_axis_chart = alt.layer(chart_1, chart_2, chart_3).resolve_scale(y = 'independent')

    return dual_axis_chart

########## -------------- Page arrangement -------------- ##########
########## ---------------------------------------------- ##########

page = st.sidebar.radio("Menu",["Home","Rice","Corn","Cassava", "Climate", "Thailand"])

#### ---- HOME ---- ####
if page == "Home":

    st.image("https://c.tadst.com/gfx/600x337/international-year-plant-health.jpg?1", width = 600)
    st.subheader("Welcome to webapp of data analysis with the historical agriculture price data recorded monthly from January 2014 to March 2019")
    st.write("Thailand is a dynamic developing country which is known for its significant contributions to global agriculture exporting. It is a major exporter of agricultural products, with a reputation for delivering their culture along with them  like rice, fruits, cassava, and fish. These agricultural exports not only deliver and serve the nation's economy but also serve as Thai culture and traditions. Additionally, they fulfill the dietary needs of the Thai population. However, the increasing prices of these fundamentals have raised concerns in understanding the intricate dynamics governing their fluctuations.")  
    st.markdown("This webapp will assist you to explore and analyze historical agriculture price data recorded from **January 2019** to **June 2019**. It is also to understand and review the trends and patterns in the price fluctuations of key agricultural products. Furthermore, our goal is to find the potential factors that influence Thailand's main agriculture pricing dynamics. While inflation undoubtedly plays an important role in driving price changes, we are particularly interested in discerning the distinct impacts of other contributing factors.")
    st.markdown("#### Data Selection")
    st.write("The core dataset for this project will focus on three fundamental agricultural products: **cassava, rice, and corn**. **Monthly price records in Bangkok from January 2001 to March 2020 will be analyzed**. In addition to this primary dataset, we will incorporate three distinct datasets, each with the potential to impact agriculture prices and inflation.")
    
    st.write("### Explore the dataset")
    raw = st.checkbox("Raw dataset of Thailand agriculture product price Monthly (2014 - 2019)")
    if raw == True:
        st.dataframe(df)
    describe = st.checkbox("Desciptive analysis")
    if describe == True:
        st.dataframe(descriptive)
    
    st.markdown("#### Factors Influencing Price Dynamics")
    st.write("For more details, you can select the Menu bar to explore more about the correlation amond the variable factors and the agriculture product rpice.")
    st.markdown("1. **Land Use and Land Cover Change Dataset**: Understanding the evolution of agricultural land use and cover over the past two decades is crucial. This dataset will provide insights into the shifting agriculture areas of each product and understand the impact from the government's agricultural policies across different years.")
    st.markdown("2. **Agricultural Production Statistics**: Annual/Monthly production statistics are significant in shaping the prices which  will assess how variations in agricultural production impact pricing dynamics.")
    st.markdown("3. **Monthly Rainfall Records**: Thailand's climate is characterized by wet and dry seasons, which can profoundly affect agricultural productivity. By analyzing monthly rainfall records, we aim to understand how climatic variations correlate with fluctuations in food prices.")
    
    st.write("### Start data analysis")
    st.write("#### Price, Agriculture Area, and Amount of Production of Rice, Corn, and Cassava")
    option = st.selectbox("Please select the option below", ["Price", "Area", "Production"])
    option = str(option)
    fig = line_plot(option)
    st.altair_chart(fig)

    st.write("#### Indepth of annual Rice, Corn, and Cassava price. You can custom the year to begin the analysis")
    agri_type = st.selectbox("Please choose the agriculture product type from the list below.", ["Rice", "Corn", "Cassava"])
    year = st.slider("Year", min_value = 2014, max_value = 2019, value = 2018, step = 1)
    fig2 = detail_plot(agri_type, year)
    st.altair_chart(fig2)

#### ---- RICE ---- ####
elif page == "Rice":
    st.write("### Rice general information and analysis")
    st.image("https://news.thaipbs.or.th/media/TSNBg3wSBdng7ijMho7k51Nzv9MyniZjx4TdAN0izb3.jpg")
    st.write("#### Rice is the main crop for Thailand. Thai people consume rice mainly everyday.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://ipad.fas.usda.gov/countrysummary/images/TH/cropprod/TH_Rice.png", width = 350)
    with col2:
        st.write("## ")
        st.write("Thailand is a prominent global rice producer and exporter, with extensive cultivation spanning 11 million hectares and contributing to over 30% of the world's rice trade volume in 2009. The government introduced the rice-pledging scheme in 2011 to support farmers by offering a higher price than the market rate for their rice.")
        st.write("Despite reduced rice harvests in 2014, continued sales from government reserves are expected to boost exports, potentially regaining the top exporter status in 2015. However, the rice sector faces sustainability challenges due to low productivity, labor shortages, and water scarcity.")
    st.write("## ")
    st.write("Rice in Thailand is primarily grown during the wet (75% rain-fed, 25% irrigated) and dry seasons. Climate change, affecting temperature and precipitation, poses risks to rain-fed cropping systems. Adaptation strategies involve altering agricultural practices, enhancing water management, diversifying agriculture, investing in technology, and implementing insurance and risk management.")
    st.write("Water shortages, linked to climate change, present a significant obstacle to increased production. As climate change impacts rice yields and global population growth threatens food security, Thailand's rice industry must address production challenges and adapt to the realities of climate change.")
    st.write("## ")

    st.write("### Correlation heatmap of rice in 2014 - 2019 with driven factor that effect the price.")
    st.write("### ")
    fig = heatmap(rice_mean)
    st.altair_chart(fig)
    st.write("### ")
    st.write("")

    fact = st.selectbox("Facts about Rice in Thailand", ["Select here", "Rice Every Meal", "Our Best Rice"])
    
    if fact == "Rice Every Meal":
        st.write("The most consumed food and a defining part of Thai cuisine. One thing is certain you will not find any locals eating a meal without rice! It is thought to have its own soul which highlights its importance in the country’s culture.")
        st.write("Symbolized by Mae Posop, or “Rice Mother”, who is born from rice, then later falls pregnant and gives birth to more rice, creating a cycle of life of its own. The prominence of rice is also emphasized by the fact that the verb “to eat” (kin khao) in Thai translates to “eat rice”. Used as a vessel that can be drenched in various curries and sauces but can also be used to null)")
    elif fact == "Our Best Rice":
        st.write("Jasmine rice, known as ข้าวหอมมะลิ (khao hom mali) in Thai, is a premium-quality rice variety extensively cultivated in Thailand. However, it is believed that only specific regions, including Surin, Buriram, and Sisaket Provinces, can produce high-quality hom mali rice. Despite its lower crop yield compared to other rice types, jasmine rice commands a significantly higher price in the global market, often selling for more than double the price of other rice cultivars.")
    elif fact == "Select here":
        st.write("  ")

#### ---- CORN ---- ####
elif page == "Corn":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://www.ตลาดเกษตรกรออนไลน์.com/uploads/products/images/img_6423d9b84d507.jpg", width = 225)
    with col2:
        st.image("https://i.pinimg.com/1200x/0b/5e/34/0b5e349d855baea9ae2c46c46ebc3b94.jpg", width = 230)
    with col3:
        st.image("https://faprathanfarm.co.th/tinymce/uploaded/Product/veggie/P44.jpg", width = 182)
    st.write("### Corn is the second main crop we grow. There are a lot of delicious Thai meal and Thai dessert made from corn.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://ipad.fas.usda.gov/countrysummary/images/TH/cropprod/TH_Corn.png")
    with col2:
        st.write("## ")
        st.write("Corn is a globally significant food source and one of Thailand's major crops, covers approximately 33% of the country's upland farmlands, with significant growth observed in northern Thailand. However, post-harvest practices involve widespread open burning to dispose of maize cobs and husks for land preparation, resulting in various issues for both local communities and urban residents.")

    st.write("## ")
    st.write("Corn is one of Thailand's five major crops, alongside rice, cassava, sugarcane, and rubber, covering a substantial portion (about 33%) of the country's upland farmlands. In 2017, Thailand's corn production reached 41 million tonnes, showing a 1.26% increase from the previous year. This increase was also reflected in corn yield, which rose to 4,500 kg/ha, marking a 5.73% increase from 4,256 kg/ha, partly due to support from the Promotion on Dry Season Corn Production after Major Rice Crop Year 2017 Project. Additionally, favorable rainfall conditions during the rainy season contributed to the improved corn yield.")
    st.write("## ")
    st.write("### Correlation heatmap of corn in 2014 - 2019 with driven factor that effect the price.")
    st.write("### ")
    fig = heatmap(corn_mean)
    st.altair_chart(fig)    

#### ---- CASSAVA ---- ####
elif page == "Cassava":

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://www.czapp.com/wp-content/uploads/2022/11/7c6a62ad-01a4-4b41-a6a0-712bd3e137fa.jpg", width = 350)
    with col2:
        st.image("https://www.opt-news.com/public/upload/news/newsa23aab22b4cd1cc9c9a8aa7194847764.jpg", width = 325)

    st.write("### Cassava is used to make the flour and of course Thai delicious traditional dessert.")
    st.write("## ")
    st.write("Cassava is a root vegetable that Plantations International grows in Thailand. It is the underground part of the cassava shrub, which has the Latin name Manihot esculenta. Like potatoes and yams, it is a tuber crop. Cassava roots have a similar shape to sweet potatoes.")
    st.write("People can also eat the leaves of the cassava plant. Humans living along the banks of the Amazon River in South America grew and consumed cassava hundreds of years before Christopher Columbus first voyaged there.")
    st.write("Cassava is a significant staple food for over 800 million people worldwide, serving as a primary dietary component in numerous countries, particularly in Sub-Saharan Africa, where it stands as a primary source of carbohydrates among staple crops. It is also a vital energy crop for bioethanol production and is well-suited to hot, lowland tropical regions and depleted soils. Thailand is a major global producer and exporter of cassava products, ranking first in export values for fresh cassava and manioc starch for the last decade, with 2019 figures accounting for 62.32% and 72.31% of global export values, respectively. In terms of cassava production and harvested area, Thailand ranks second and third globally, producing 32 million tons from 1.38 million hectares in 2018. At the local level, around 0.46 million farm households cultivate cassava, with a million hectares of harvested area, making it the fourth most widely cultivated crop in the country in terms of cropland use.")
    st.write("## ")
    st.write("### Correlation heatmap of cassava in 2014 - 2019 with driven factor that effect the price.")
    st.write("### ")
    fig = heatmap(cassava_mean)
    st.altair_chart(fig)

#### ---- CLIMATE ---- ####
elif page == "Climate":
    st.image("https://thepattayanews.com/wp-content/uploads/2023/05/5ff66a95ac7c84ed5b190efba0db9b1d-1.jpg?v=1684740443")
    st.write("### Climate is another issue that need to be considered")
    st.write("### ")
    col1, col2 = st.columns(2)
    with col1:
        st.write("This graph is interactve bar chart represents the precipitation (including rainfall) in mm per year, and line plot represents yearly mean surface temperature.")
        st.write("Mean annual rainfall is 1,200-4,500 mm, with lower totals on the leeward side and higher totals on the windward side. Mean temperature is 26.3°C in the north and 27.5°C in the southern and coastal areas.")
        st.write("In 2017, the precipitation record is the highest in value compares to other years.")
    with col2:
        fig = precip_plot(cassava_mean)
        st.altair_chart(fig)

#### ---- THAILAND ---- ####
elif page == "Thailand":
    st.image("https://www.marketinginasia.com/wp-content/uploads/2023/07/Why-Thailand-Could-Emerge-as-a-Leading-IT-Production-Powerhouse.jpg")
    st.write("### Thailand is one of the South East Asia country located near the equation. It is the dream tourist destinations for many tourists because of the beaasutiful landscape that blending well with the culture")
    
