from serpapi import GoogleSearch
def get_company_website(company_name):
    params = {
        "engine": "google",
        "q": f"{company_name} site:linkedin.com OR site:crunchbase.com",
        "api_key": "10ec53f23ad25e383cc9df5d600e31691091f5de162c81a5c21e77bafb604f2d"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    for result in results.get("organic_results", []):
        link = result.get("link", "")
        if "linkedin.com" in link or "crunchbase.com" in link:
            return link
    return "Not Found"
