# questionnaire.py

import streamlit as st

def get_questionnaire_responses():
    countries = [
        "United States", "Canada", "United Kingdom", "Germany", "France", "India",
        "China", "Japan", "Brazil", "Australia", "South Africa", "Mexico",
        "Italy", "Spain", "Netherlands", "Russia", "South Korea", "Singapore",
        "Saudi Arabia", "Sweden", "Switzerland", "United Arab Emirates"
    ]

    questionnaire = {
        "general_info": {
            "company_name": st.text_input("Company Name"),
            "industry": st.text_input("Industry"),
            "number_of_employees": st.number_input("Number of Employees", min_value=1),
            "annual_revenue": st.number_input("Annual Revenue", min_value=0.0),
            "geographic_presence": st.multiselect("Geographic Presence (Select Regions/Countries)", options=countries),
            "primary_products": st.text_input("Primary Products/Services")
        },
        "sales_strategy": {
            "current_sales_strategy": st.text_input("Describe your current sales strategy"),
            "target_market": st.text_input("What is your target market(s)?"),
            "prospect_prioritization": st.text_input("How do you identify and prioritize prospects?"),
            "lead_generation_methods": st.text_input("What methods do you use for lead generation?"),
            "prospecting_outreach": st.text_input("What is your sales team's approach to prospecting and outreach?")
        },
        "marketing_strategy": {
            "current_marketing_strategy": st.text_input("Describe your current marketing strategy"),
            "marketing_channels": st.text_input("What marketing channels do you utilize (e.g., digital, print, events)?"),
            "lead_nurturing": st.text_input("How do you generate and nurture leads?"),
            "content_strategy": st.text_input("What is your content marketing strategy?"),
            "campaign_effectiveness": st.text_input("How do you measure the effectiveness of your marketing campaigns?")
        },
        "customer_engagement": {
            "engage_prospects": st.text_input("How do you engage with prospective customers?"),
            "customer_relationships": st.text_input("How do you maintain relationships with existing customers?"),
            "feedback_utilization": st.text_input("How do you collect and utilize customer feedback?"),
            "retention_strategies": st.text_input("What customer retention strategies do you have in place?")
        },
        "sales_process": {
            "sales_process_outline": st.text_input("Outline your sales process from lead generation to closing deals"),
            "lead_qualification": st.text_input("How do you qualify leads?"),
            "automation_crm_tools": st.text_input("What tools or technologies do you use for sales automation or CRM?"),
            "objection_handling": st.text_input("How do you handle objections and negotiations?")
        },
        "marketing_assets": {
            "collateral_description": st.text_input("Describe your marketing collateral and assets (e.g., brochures, presentations, website)"),
            "messaging_consistency": st.text_input("How do you ensure consistency in messaging and branding across different channels?")
        },
        "performance_metrics": {
            "sales_kpis_tracked": st.text_input("What key performance indicators (KPIs) do you track for sales?"),
            "marketing_kpis_tracked": st.text_input("What KPIs do you track for marketing?"),
            "metrics_analysis_frequency": st.text_input("How frequently do you analyze and review these metrics?")
        },
        "integration_alignment": {
            "sales_marketing_alignment": st.text_input("How aligned are your sales and marketing teams?"),
            "alignment_ensurance": st.text_input("How do you ensure alignment between sales and marketing efforts?"),
            "integration_challenges": st.text_input("Are there any challenges or barriers to integration?")
        },
        "competitive_landscape": {
            "main_competitors": st.text_input("Who are your main competitors?"),
            "competitive_advantage": st.text_input("What sets you apart from your competitors in terms of sales and marketing?")
        },
        "future_goals": {
            "short_term_goals": st.text_input("What are your short-term and long-term sales and marketing goals?"),
            "goal_steps": st.text_input("What steps are you taking to achieve these goals?")
        },
        "additional_insights": {
            "comments": st.text_area("Please provide any additional comments, insights, or challenges related to your B2B Sales & Marketing efforts")
        }
    }
    return questionnaire
