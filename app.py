import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('world_happiness_2015_2023.csv')

st.set_page_config(page_title="World Happiness Report", layout="centered")

st.title("🌍 World Happiness Report (2015–2023)")
st.markdown("Explore global happiness trends by GDP, life expectancy, and over time.")

# Sidebar year filter
year = st.sidebar.selectbox("Select a year", sorted(df['Year'].unique()))
filtered_df = df[df['Year'] == year]

# Scatterplot: GDP vs. Happiness
st.subheader(f"Happiness vs. GDP per Capita ({year})")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x='GDP_perCapita', y='HappinessScore', ax=ax1)
ax1.set_title("Happiness vs. GDP per Capita")
st.pyplot(fig1)

# Scatterplot: Life Expectancy vs. Happiness
st.subheader(f"Happiness vs. Healthy Life Expectancy ({year})")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='HealthyLifeExpectancy', y='HappinessScore', ax=ax2)
ax2.set_title("Happiness vs. Healthy Life Expectancy")
st.pyplot(fig2)

# Line plot for selected countries
st.subheader("Happiness Over Time – Selected Countries")
selected_countries = ['Finland', 'Israel', 'Germany', 'United States', 'Japan']
subset = df[df['Country'].isin(selected_countries)]

fig3, ax3 = plt.subplots()
sns.lineplot(data=subset, x='Year', y='HappinessScore', hue='Country', marker='o', ax=ax3)
ax3.set_title("Happiness Score Over Time")
st.pyplot(fig3)

st.markdown("---")
st.caption("Created for the ITDS 2025 Midterm Project – Reichman University")