import requests
import logging

def extract_users(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        logging.info("API data extracted successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API extraction failed: {e}")
        return []
