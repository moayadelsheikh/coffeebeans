# ☕ Coffee Beans Sales Analysis Dashboard

An interactive end-to-end data engineering and visualization project. This dashboard analyzes global coffee sales, product performance, and customer loyalty using Python, Pandas, and Streamlit.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

---

## 🚀 Project Overview
This project transforms raw coffee sales data into actionable business insights. It features a modular data pipeline and a responsive dashboard to help stakeholders understand market trends.

### Key Business Questions Addressed:
* **Revenue Trends:** How do sales and net profit fluctuate month-over-month?
* **Market Share:** Which countries and cities are the top revenue generators?
* **Product Performance:** Which coffee type (Arabica, Robusta, etc.) and roast level perform best?
* **Customer Loyalty:** Who are the top 10 high-value customers?
* **Inventory Insights:** Analysis of sales by package size (0.5kg to 2.5kg).

---

## 🏗️ Project Structure
The project follows a modular "Data Engineering" approach:

```text
├── cleaned data/       # Processed .pkl and .parquet files
├── app.py              # Main Streamlit dashboard script
├── data_processing.py  # Modular cleaning and transformation pipeline
├── main.ipynb          # Exploratory Data Analysis (EDA) notebook
└── requirements.txt    # Project dependencies
