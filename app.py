# 1. Look at your dataset and determine 3 things you would want to track as a stakeholder.
# (1) How does temperature correlate with weekly sales?
# (2) How do fuel prices correlate with weekly sales?
# (3) How does unemployment correlate with weekly sales?

# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# import data
df = pd.read_csv('Walmart_Sales (1).csv')

# 2. Wrangle and Prepare Your Data

# Print the data to see how it looks and also to see the names of the column headers
print(df.columns)

# Handling missing values
df = pd.read_csv('Walmart_Sales (1).csv')

# Remove rows with missing values
df.dropna(inplace=True)

#round values in temperature, fuel price, cpi, and unemployment columns for simplicity
df['Temperature'] = df['Temperature'].round(0)
df['Fuel_Price'] = df['Fuel_Price'].round(2)
df['CPI'] = df['CPI'].round(0)
df['Unemployment'] = df['Unemployment'].round(1)

#Rename holiday column for simplicity
df.rename(columns={'Holiday_Flag': 'Holiday'}, inplace=True)


#extract additional features such as year and month from the timestamp for more options in using the data
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
print(df.head())

# Title of the web app
st.title("Factors Influencing Walmart Sales")

# Main content
st.caption("Data source: https://www.kaggle.com/datasets/mikhail1681/walmart-sales")
st.write("Dear Walmart Shareholder: Here we will go over various factors influencing weekly sales.")
st.dataframe(df)

# I wish I had more time to be able to work on this, but I do not.

# The next thing I would have done is try to make 3 separate graphs that go along with what I listed above as the 3 things I would like to track as a stakeholder.

# The first graph would show how temperature correlates with weekly sales.
# The Date would be on the x-axis. Temperature and Weekly Sales would be on the y-axis.

# The second graph would show how fuel prices correlate with weekly sales.
# The Date would be on the x-axis. Fuel Prices and Weekly Sales would be on the y-axis.

# The third graph would show how unemployment correlates with weekly sales.
# The Date would be on the x-axis. Unemployment and Weekly Sales would be on the y-axis.

# Finally, I would build the dashboard to make it as simple as possible for the shareholders to interact with for future decision making.
# Then I would deploy the app so they could interact with it.

# Run the app with: streamlit run app.py
# python -m streamlit run app.py
