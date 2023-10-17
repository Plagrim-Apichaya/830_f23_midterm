import streamlit as st
import seaborn as sns
import pandas as pd

st.write("""
# WI cancer dataset
Explore the relationship among the dataset?
""")

x_axis = st.selectbox(
    'Choose your x variable',
    ('radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst'))

st.write('You selected x variable:', x_axis)

y_axis = st.selectbox(
    'Choose your y variable',
    ('radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst'))

st.write('You y variable:', y_axis)

WI_df = pd.read_csv('data.csv') 

#WI_df.head()
#WI_df['diagnosis'] = WI_df[['diagnosis']].applymap(lambda x: 0 if x=='B' else 1)
#WI_df['diagnosis'] = pd.to_numeric(WI_df['diagnosis'])

#corr = WI_df.corr()

#high_corr = corr.diagnosis[(corr['diagnosis'] > 0.7) | (corr['diagnosis'] < -0.7)]
#cols_max_corr = list(high_corr.index)
#high_corr_df = WI_df.loc[:,cols_max_corr]

afig1 = sns.lmplot(data=WI_df, x=x_axis, y=y_axis, hue='diagnosis')
st.pyplot(afig1)