import streamlit as st
import pandas as pd
from scraper import get_company_website
from ai_readiness import get_ai_score

st.title("🔍AI-Ready Lead Generation Tool")

company_name = st.text_input("Enter Company Name")
if st.button("Analyze"):
    with st.spinner("Searching and analyzing..."):
        website = get_company_website(company_name)
        ai_score = get_ai_score(f"{company_name} uses AI to optimize operations.")  # Simulate content
        st.success(f"Website: {website}")
        st.info(f"AI Readiness Score: {ai_score}")

        new_row = pd.DataFrame([{
            "Company": company_name,
            "Website": website,
            "AI Readiness Score": ai_score
        }])
        new_row.to_csv("leads.csv", mode="a", index=False, header=False)
        st.write(new_row)
