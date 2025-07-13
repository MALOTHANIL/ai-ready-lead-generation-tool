
# AI-Ready Lead Generation scoring Tool

This tool helps you identify AI-ready companies by searching for their LinkedIn or Crunchbase pages and assigning an AI Readiness Score based on their description or simulated AI signals. It's ideal for investors, analysts, or sales teams seeking high-impact, tech-forward leads.
 Search for a company’s public profile (LinkedIn/Crunchbase) using SerpAPI
 Simulated AI Readiness scoring
 Save results to a CSV file (`leads.csv`)
Clean and simple Streamlit user interface

#Required packages:
streamlit
pandas
serpapi
beautifulsoup4
requests
gemini api
#Sample Use Case
Input: OpenAI

Output:

Website: https://www.linkedin.com/company/openai

AI Readiness Score: 9

This tool is built for:

M&A analysts assessing digital maturity investment 

Investors screening for high-potential AI-enabled companies

Sales teams identifying AI-forward B2B leads

# project overview 
                    ┌────────────────────┐
                    │  User Enters Name  │
                    │  e.g., "Acme Corp" │
                    └────────┬───────────┘
                             │
                             ▼
               ┌─────────────────────────┐
               │ Scraper searches Google/web scraping │
               │ → Finds website, LinkedIn │
               └────────┬────────────────┘
                        │
                        ▼
         ┌──────────────────────────────┐
         │ Fetches text from the website│
         └────────┬─────────────────────┘
                  │
                  ▼
        ┌─────────────────────────────┐
        │ Send text to Gemini/OpenAI  │
        │ → "Rate AI-readiness"       │
        └────────┬────────────────────┘
                 │
                 ▼
         ┌─────────────────────────────┐
         │ Score & Summary are returned│
         │ e.g., "8/10, uses AI in ops"│
         └────────┬────────────────────┘
                 ▼
        ┌──────────────────────────────┐
        │ Display result in table +    │
        │ Allow download as CSV        │
        └──────────────────────────────┘

