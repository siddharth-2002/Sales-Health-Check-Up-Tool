# report_generator.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from kpi_calculator import calculate_kpis
from reportlab.lib.utils import ImageReader

industry_benchmark = {
    "lead_generation": 4,
    "customer_engagement": 4,
    "conversion_rate": 4,
    "sales_cycle_length": 3.5,
    "retention_rate": 4,
    "revenue_growth": 4.5,
    "customer_satisfaction": 4
}

def generate_recommendations(kpi_scores, responses):
    recommendations = []
    
    # Threshold to identify weak KPIs
    low_threshold = 3

    # Determine company size based on number of employees
    company_size = int(responses["general_info"].get("number_of_employees", 0))
    size_category = "small" if company_size < 50 else "medium" if company_size <= 250 else "large"
    
    # Get industry from responses
    industry = responses["general_info"].get("industry", "").lower()

    # Recommendations based on KPI scores
    if kpi_scores.get("conversion_rate", 0) < low_threshold:
        recommendations.append("Improve Conversion Rate: Implement targeted lead nurturing and personalized outreach strategies. Consider using CRM tools to analyze lead behavior and increase follow-ups to boost conversion rates.")
    
    if kpi_scores.get("customer_engagement", 0) < low_threshold:
        recommendations.append("Enhance Customer Engagement: Use personalized email campaigns, interactive content, and consistent follow-ups. Implement a feedback system to better understand customer needs and adjust engagement strategies accordingly.")

    if kpi_scores.get("retention_rate", 0) < low_threshold:
        recommendations.append("Boost Customer Retention: Introduce loyalty programs, offer discounts for repeat purchases, and conduct regular check-ins. Consider surveying customers to identify key areas of satisfaction and dissatisfaction.")

    if kpi_scores.get("sales_cycle_length", 0) < low_threshold:
        recommendations.append("Reduce Sales Cycle Length: Use automation tools to streamline communication and follow-ups. Train the sales team to focus on high-quality leads and reduce time spent on low-probability prospects.")

    if kpi_scores.get("revenue_growth", 0) < low_threshold:
        recommendations.append("Increase Revenue Growth: Consider expanding into new markets, developing new product features, or creating a tiered pricing structure. Investing in targeted marketing campaigns could also attract more customers.")

    if kpi_scores.get("customer_satisfaction", 0) < low_threshold:
        recommendations.append("Improve Customer Satisfaction: Conduct regular surveys to capture feedback and quickly resolve issues. Implement a ticketing system to track customer inquiries and provide prompt responses.")

    # Industry-specific recommendations
    if industry == "technology" and kpi_scores.get("conversion_rate", 0) < low_threshold:
        recommendations.append("Leverage AI in Conversion: Implement AI-driven lead scoring and predictive analytics to identify and focus on high-potential leads. This will help the sales team prioritize and improve conversion rates.")
    
    if industry == "retail" and kpi_scores.get("retention_rate", 0) < low_threshold:
        recommendations.append("Loyalty Programs for Retail: Introduce a customer loyalty program offering exclusive discounts and rewards. This will encourage repeat purchases and improve retention.")

    if industry == "healthcare" and kpi_scores.get("customer_satisfaction", 0) < low_threshold:
        recommendations.append("Enhance Patient Support: Create patient follow-up protocols and offer personalized care to improve satisfaction. Implement post-service feedback to monitor patient experience.")

    # Company size-specific recommendations
    if size_category == "small" and kpi_scores.get("lead_generation", 0) < low_threshold:
        recommendations.append("Affordable Lead Generation: Focus on cost-effective digital marketing, like social media and SEO, to reach a larger audience without a significant financial investment.")

    if size_category == "medium" and kpi_scores.get("customer_engagement", 0) < low_threshold:
        recommendations.append("Invest in CRM for Engagement: Utilize a CRM system to track customer interactions and follow-up reminders to ensure consistent engagement.")

    if size_category == "large" and kpi_scores.get("revenue_growth", 0) < low_threshold:
        recommendations.append("Expand to New Markets: Large companies can consider entering untapped markets or acquiring smaller companies to grow revenue and expand market share.")

    # Default recommendation if no other conditions are met
    if not recommendations:
        recommendations.append("Maintain current strategies and prioritize continuous improvement in key areas.")

    # Join recommendations into a single string for display in the PDF
    return " ".join(recommendations[:3])

def generate_pdf_report(sales_data, selected_kpis, responses, filename="Sales_Health_Checkup_Report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    logo_path = "logo.png"
    logo = ImageReader(logo_path)
    c.drawImage(logo, x=width - 2 * inch, y=height - 1 * inch, width=1.5 * inch, height=1 * inch)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "SALES HEALTH CHECK-UP REPORT")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, "Key Performance Indicators (KPIs)")

    c.setFont("Helvetica-Bold", 10)
    y = height - 100
    c.drawString(50, y, "KPI")
    c.drawString(200, y, "Absolute Value")
    c.drawString(300, y, "Score (1-5)")
    c.drawString(380, y, "Industry Benchmark (1-5)")
    c.drawString(470, y, "Overall Sales Health Score")
    c.drawString(570, y, "Overall Industry Benchmark Score")

    y -= 20
    kpi_scores = calculate_kpis(sales_data, selected_kpis)
    for kpi in selected_kpis:
        score = kpi_scores.get(kpi, "N/A")
        benchmark = industry_benchmark.get(kpi, "N/A")
        
        c.setFont("Helvetica", 10)
        c.drawString(50, y, kpi.replace("_", " ").title())
        c.drawString(200, y, str(score))
        c.drawString(300, y, f"{score}/5")
        c.drawString(380, y, f"{benchmark}/5")
        c.drawString(470, y, str(score))  
        c.drawString(570, y, str(benchmark))
        y -= 15

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "ASSESSMENT SUMMARY:")

    c.setFont("Helvetica", 10)
    y -= 20
    c.drawString(50, y, "1. BRIEF SUMMARY OF ASSESSMENT FINDINGS")
    y -= 15
    c.drawString(60, y, "The overall sales health is strong, with significant achievements in Revenue Growth.")
    
    y -= 20
    c.drawString(50, y, "2. KEY STRENGTHS OBSERVED")
    y -= 15
    c.drawString(60, y, "- Strong Revenue Growth and Customer Satisfaction")
    
    y -= 20
    c.drawString(50, y, "3. AREAS FOR IMPROVEMENT IDENTIFIED")
    y -= 15
    c.drawString(60, y, "- Low Conversion Rate and Customer Engagement need attention")

    y -= 20
    c.drawString(50, y, "4. RECOMMENDATIONS FOR ENHANCING SALES PERFORMANCE")
    y -= 15
    recommendations_text = generate_recommendations(kpi_scores, responses)
    c.drawString(60, y, recommendations_text)

    c.save()
    print(f"Report generated: {filename}")
