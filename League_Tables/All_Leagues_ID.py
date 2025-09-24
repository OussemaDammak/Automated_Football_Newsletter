import requests

def get_leagues_id(api_key):
    url = f"https://apiv2.allsportsapi.com/football/?met=Leagues&&APIkey={api_key}"
    response = requests.get(url)
    data = response.json()
    countries_list = []

    if data.get("success") == 1:
        for country in data.get("result", []):
            if country.get("country_name") == "Tunisia":
                countries_list.append({
                    "key": country.get("league_key"),
                    "name": country.get("league_name"),
                    "country": country.get("country_name")
            })
    return countries_list