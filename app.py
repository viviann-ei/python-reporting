import psycopg2
import pandas as pd
import streamlit as st
import plotly.express as px

# -------------------------
# Database connection
# -------------------------
conn = psycopg2.connect(
    host="localhost",
    database="pagila_dwh",
    user="viviannigbokwe"
)

# -------------------------
# Streamlit App
# -------------------------
st.title("Pagila DWH – Python Reporting")

st.markdown("""
This app shows two reports from the Pagila Data Warehouse:
1. Rentals by film category  
2. Rental trends over time  
""")

# -------------------------
# Report 1: Rentals by Film Category
# -------------------------
query_category = """
SELECT film_category,
       COUNT(*) AS total_rentals,
       SUM(rental_amount) AS total_revenue
FROM vw_rental_analysis
GROUP BY film_category
ORDER BY total_rentals DESC;
"""

df_category = pd.read_sql(query_category, conn)

st.subheader("Report 1: Rentals by Film Category")

fig1 = px.bar(
    df_category,
    x="film_category",
    y="total_rentals",
    title="Total Rentals by Film Category"
)

st.plotly_chart(fig1)

# -------------------------
# Report 2: Rental Trends Over Time
# -------------------------
query_time = """
SELECT year, month, month_name,
       COUNT(*) AS total_rentals,
       SUM(rental_amount) AS total_revenue
FROM vw_rental_analysis
GROUP BY year, month, month_name
ORDER BY year, month;
"""

df_time = pd.read_sql(query_time, conn)

# Create a readable time column
df_time["year_month"] = df_time["year"].astype(str) + "-" + df_time["month"].astype(str)

st.subheader("Report 2: Rental Trends Over Time")

fig2 = px.line(
    df_time,
    x="year_month",
    y="total_rentals",
    title="Monthly Rental Trends"
)

st.plotly_chart(fig2)

conn.close()
