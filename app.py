import requests
import os
from fastapi import FastAPI, Query
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


API_KEY = os.getenv('API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')


def get_company_detail(company_name, location):

    search_query = f"{company_name} {location}"

    # Google API
    url = 'https://www.googleapis.com/customsearch/v1'

    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        try:
            results = response.json()
            if 'items' in results:
                return results['items']
            else:
                return {"message": "No results found"}
        except:
            return {"error": "Failed to decode JSON", "content": response.text}
    else:
        return {"error": f"Request failed with status code: {response.status_code}", "content": response.text}


@app.get("/search-company/")
def search_company(
    company_name: str = Query("Evolvision Technologies"),
    location: str = Query("Gandhinagar")
):
    search_results = get_company_detail(company_name, location)
    return search_results
