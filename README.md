# Python Reporting with Pagila DWH

## Project Overview
This project was created as part of the course **Data Management, Analysis and Reporting (DMAR)**.
It demonstrates a simple Python reporting application using the Pagila Data Warehouse.

The application connects to a PostgreSQL database and generates two reports with visualizations.

---

## Reports

### Report 1: Rentals by Film Category
- Bar chart
- X-axis: Film category
- Y-axis: Total number of rentals

### Report 2: Rental Trends Over Time
- Line chart
- X-axis: Time (year and month)
- Y-axis: Total number of rentals

---

## Technologies Used
- Python 3
- PostgreSQL (Pagila DWH)
- psycopg2
- pandas
- Streamlit
- Plotly

---

## AI-Assisted Development

### AI Tool Used
ChatGPT was used as an AI assistant to support the development of the application.

### Main Prompts
- “Create a minimal Streamlit app that connects to a PostgreSQL database pagila_dwh and queries the view vw_rental_analysis.”
- “Write an SQL query that groups rental data by film category and returns total rentals as a pandas DataFrame.”
- “Create two charts in Streamlit: a bar chart for rentals by category and a line chart for monthly rental trends.”

### What Worked Well / What Was Challenging
Using AI worked well for quickly generating SQL queries and Streamlit visualization code.
The main challenges were environment setup and configuring GitHub authentication, which required several iterations to resolve.

---

## Screenshots
Screenshots of both reports are available in the Screenshots folder.

---

## How to Run the Application
```bash
python3 -m pip install streamlit pandas plotly psycopg2-binary
python3 -m streamlit run app.py
