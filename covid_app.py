import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set style
sns.set(style="whitegrid")
st.set_page_config(layout="wide")

# Title
st.title("🌍 COVID-19 Data Explorer")
st.markdown("Visualize global COVID-19 trends: Cases, Deaths, and Vaccination Progress")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# Country selection
all_countries = df["location"].unique().tolist()
countries = st.multiselect("Select countries to analyze", all_countries, default=["Nigeria", "India", "United States"])

# Filter data
filtered_df = df[df["location"].isin(countries)]

# Line plot: Total Cases
st.subheader("📈 Total COVID-19 Cases Over Time")
fig_cases, ax = plt.subplots()
for country in countries:
    country_df = filtered_df[filtered_df["location"] == country]
    ax.plot(country_df["date"], country_df["total_cases"], label=country)
ax.set_title("Total Cases")
ax.set_xlabel("Date")
ax.set_ylabel("Total Cases")
ax.legend()
st.pyplot(fig_cases)

# Line plot: Total Deaths
st.subheader("💀 Total COVID-19 Deaths Over Time")
fig_deaths, ax = plt.subplots()
for country in countries:
    country_df = filtered_df[filtered_df["location"] == country]
    ax.plot(country_df["date"], country_df["total_deaths"], label=country)
ax.set_title("Total Deaths")
ax.set_xlabel("Date")
ax.set_ylabel("Total Deaths")
ax.legend()
st.pyplot(fig_deaths)

# Plot: Vaccination Progress
st.subheader("💉 Vaccination Progress (% Fully Vaccinated)")
fig_vax, ax = plt.subplots()
for country in countries:
    country_df = filtered_df[filtered_df["location"] == country]
    ax.plot(country_df["date"], country_df["people_fully_vaccinated_per_hundred"], label=country)
ax.set_title("Fully Vaccinated per 100 People")
ax.set_xlabel("Date")
ax.set_ylabel("% Fully Vaccinated")
ax.legend()
st.pyplot(fig_vax)

# Choropleth Map
st.subheader("🌐 Vaccination Rates by Country (Latest Data)")
latest = df[df["date"] == df["date"].max()]
fig_map = px.choropleth(latest,
                        locations="iso_code",
                        color="people_fully_vaccinated_per_hundred",
                        hover_name="location",
                        color_continuous_scale="Plasma",
                        title="Latest Vaccination Rates")
st.plotly_chart(fig_map)
