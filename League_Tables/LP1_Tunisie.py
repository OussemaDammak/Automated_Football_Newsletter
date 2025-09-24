import requests

def LP1_standing(api_key):
    url = f"https://apiv2.allsportsapi.com/football/?&met=Standings&leagueId=317&APIkey={api_key}"
    response = requests.get(url)
    data = response.json()
    countries_list = []

    if data.get("success") == 1:
        for country in data["result"]["total"]:
            countries_list.append({
                "standing_place": country.get("standing_place"),
                "standing_team": country.get("standing_team"),
                "Points": country.get("standing_PTS"),

            })
    return countries_list