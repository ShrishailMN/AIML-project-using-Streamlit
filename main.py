import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Generate Random Data for Air Quality and Water Pollution
np.random.seed(42)
n_countries = 20
countries = [f'Country {i}' for i in range(1, n_countries + 1)]

air_quality_data = pd.DataFrame({
    'Country': np.random.choice(countries, size=100),
    'Year': np.random.choice(range(2010, 2023), size=100),
    'AirQualityIndex': np.random.randint(30, 150, size=100),
})

water_pollution_data = pd.DataFrame({
    'Country': np.random.choice(countries, size=100),
    'Year': np.random.choice(range(2010, 2023), size=100),
    'WaterPollutionIndex': np.random.randint(20, 120, size=100),
})

# Streamlit App
st.title('World Air Quality and Water Pollution Visualization')

# Sidebar for User Input
st.sidebar.header('User Input')
selected_chart = st.sidebar.selectbox('Select Chart Type', ['Line Chart', 'Bar Chart', 'Scatter Plot', 'Map'])

# Main Content
st.header('Randomly Generated Data:')
st.subheader('Air Quality Data:')
st.dataframe(air_quality_data.head())

st.subheader('Water Pollution Data:')
st.dataframe(water_pollution_data.head())

st.header('Selected Chart:')
if selected_chart == 'Line Chart':
    fig = px.line(air_quality_data, x='Year', y='AirQualityIndex', color='Country', title='Air Quality Over Time')
elif selected_chart == 'Bar Chart':
    fig = px.bar(water_pollution_data, x='Year', y='WaterPollutionIndex', color='Country', title='Water Pollution Over Time')
elif selected_chart == 'Scatter Plot':
    fig = px.scatter(air_quality_data, x='AirQualityIndex', y='Year', color='Country', title='Scatter Plot of Air Quality')
    
elif selected_chart == 'Map':
    fig = px.scatter_geo(air_quality_data, locations='Country', locationmode='country names', color='AirQualityIndex',
                         title='Air Quality Map', projection='natural earth')
    fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")

st.plotly_chart(fig)
