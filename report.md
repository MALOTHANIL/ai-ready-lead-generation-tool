# project approches:
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

