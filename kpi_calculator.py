# kpi_calculator.py

import pandas as pd

def load_sales_data(filename=None):
    if filename:
        sales_data = pd.read_csv(filename).iloc[0].to_dict()
    else:
        sales_data = {
            'leads_generated': 120,
            'sales_team_size': 10,
            'customer_engagements': 80,
            'total_customers': 200,
            'deals_closed': 30,
            'average_sales_cycle_length': 25,
            'customers_retained': 150,
            'customers_acquired': 180,
            'current_revenue': 500000,
            'previous_revenue': 450000,
            'customer_satisfaction_score': 4.5
        }
    return sales_data

def calculate_kpis(sales_data, selected_kpis):
    kpi_scores = {}
    
    if "lead_generation" in selected_kpis:
        lead_generation = sales_data['leads_generated'] / sales_data['sales_team_size']
        kpi_scores["lead_generation"] = round(lead_generation, 2) * 5
    
    if "customer_engagement" in selected_kpis:
        customer_engagement = sales_data['customer_engagements'] / sales_data['total_customers']
        kpi_scores["customer_engagement"] = round(customer_engagement, 2) * 5
    
    if "conversion_rate" in selected_kpis:
        conversion_rate = sales_data['deals_closed'] / sales_data['leads_generated']
        kpi_scores["conversion_rate"] = round(conversion_rate, 2) * 5
    
    if "sales_cycle_length" in selected_kpis:
        sales_cycle_length = sales_data['average_sales_cycle_length']
        kpi_scores["sales_cycle_length"] = 5 - (sales_cycle_length / 30)
    
    if "retention_rate" in selected_kpis:
        retention_rate = sales_data['customers_retained'] / sales_data['customers_acquired']
        kpi_scores["retention_rate"] = round(retention_rate, 2) * 5
    
    if "revenue_growth" in selected_kpis:
        revenue_growth = sales_data['current_revenue'] / sales_data['previous_revenue']
        kpi_scores["revenue_growth"] = round(revenue_growth, 2) * 5
    
    if "customer_satisfaction" in selected_kpis:
        customer_satisfaction = sales_data['customer_satisfaction_score']
        kpi_scores["customer_satisfaction"] = customer_satisfaction
    
    return {k: min(max(v, 0), 5) for k, v in kpi_scores.items()}
