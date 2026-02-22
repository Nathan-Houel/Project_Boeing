'''
Project Boeing - Flight Operations Dashboard

Houel Nathan - 20 February 2026
'''

# Import librairies
import pandas as pd
import streamlit as st

# Title of the Streamlit
st.title("Flight Operations Dashboard ✈️")

# Loading data into a dataframe
delay_flights = pd.read_csv("data/DelayedFlights_reduce.csv", index_col="Unnamed: 0")

# Extract airlines without duplicates
airlines = delay_flights["UniqueCarrier"].unique()

# Sidebar configuration
airline_select = st.selectbox("Choose an airline", airlines)
filtered_flights = delay_flights[delay_flights['UniqueCarrier'] == airline_select]

# Displaying df on Streamlit
st.dataframe(filtered_flights.head())

# Displaying KPIs
col1, col2 = st.columns(2)
number_flights = len(filtered_flights)
col1.metric("Total Flights", number_flights)

avg_delay = round(filtered_flights["ArrDelay"].mean(), 1)
col2.metric("Average Delay (min)", avg_delay)

# Graph showing causes of delays 
delay_total = (filtered_flights[['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']] > 0).sum()
st.subheader("Distribution of causes of delay")
st.bar_chart(delay_total, color="#1E90FF")

# Graph showing delay during the week
avg_delay_by_day = filtered_flights.groupby("DayOfWeek")['ArrDelay'].mean()
st.subheader("Evolution of delay during the week")
st.line_chart(avg_delay_by_day, color="#1E90FF")

# Top 5 airports with most delay
top_5_airports = filtered_flights.groupby("Origin")['ArrDelay'].mean().sort_values(ascending=False).head()
st.subheader("Top 5 airports with the highest average delays")
st.bar_chart(top_5_airports, color="#1E90FF")