import requests

def get_countries(api_key):
    url = f"https://apiv2.allsportsapi.com/football/?met=Countries&APIkey={api_key}"
    response = requests.get(url)
    data = response.json()
    countries_list = []

    if data.get("success") == 1:
        for country in data.get("result", []):
            countries_list.append({
                "key": country.get("country_key"),
                "name": country.get("country_name"),
                "logo": country.get("country_logo")
            })
    return countries_list