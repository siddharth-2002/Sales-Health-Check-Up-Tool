# app.py

import streamlit as st
import os
import pandas as pd
from report_generator import generate_pdf_report
from kpi_calculator import load_sales_data
from questionnaire import get_questionnaire_responses

# Streamlit app setup
st.title("Sales Health Check-Up Tool")

# Choose data source
st.write("### Choose Data Source")
use_sample_data = st.radio("Would you like to use the sample data or upload your own data?", ('Use Sample Data', 'Upload CSV'))

# Load data based on user choice
if use_sample_data == 'Upload CSV':
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        sales_data = pd.read_csv(uploaded_file).iloc[0].to_dict()
    else:
        sales_data = load_sales_data()  # Fallback to sample data if no file is uploaded
else:
    sales_data = load_sales_data()

# Display loaded data for verification
st.write("### Data for KPI Calculation")
st.write(pd.DataFrame([sales_data]))

# Collect questionnaire responses
st.write("### B2B Sales & Marketing Health Assessment Questionnaire")
responses = get_questionnaire_responses()

# KPI selection
st.write("### Select KPIs to Include in the Report")
available_kpis = [
    "lead_generation", "customer_engagement", "conversion_rate", 
    "sales_cycle_length", "retention_rate", "revenue_growth", 
    "customer_satisfaction"
]
selected_kpis = st.multiselect("Choose KPIs for the report:", available_kpis, default=available_kpis)

# Generate PDF Report
if st.button("Generate PDF Report"):
    generate_pdf_report(sales_data, selected_kpis, responses)
    st.success("PDF report generated successfully!")
    with open("Sales_Health_Checkup_Report.pdf", "rb") as pdf_file:
        st.download_button("Download the PDF Report", pdf_file, "Sales_Health_Checkup_Report.pdf")
