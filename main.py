import requests

API_KEY = "c19cd4f436479caba5e362f0d6e852f1ba604e2f559a8a6f049202dd0a6bd90b"

url = f"https://apiv2.allsportsapi.com/football/?met=Countries&APIkey={API_KEY}"

from fetchcountries import get_countries
from League_Tables.All_Leagues_ID import get_leagues_id
from League_Tables.LP1_Tunisie import LP1_standing
countries = get_countries(API_KEY)

for c in countries:
    print(f"{c['key']}: {c['name']} → {c['logo']}")

Leagues=get_leagues_id(API_KEY)
for l in Leagues:
    print(f"{l['key']}: {l['name']} → {l['country']}")

LP1_standing=LP1_standing(API_KEY)
for l in LP1_standing:
    print(f"{l['standing_place']}: {l['standing_team']} : {l['Points']} Pts")