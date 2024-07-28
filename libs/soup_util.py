from bs4 import BeautifulSoup
import requests

class RequestsUtil:
    def fetch(url, timeout=30):
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code != 200:
                print(f"Request failed with status code {response.status_code}")
                return None
            return BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.Timeout:
            print("The request timed out")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None