import requests
import json
import pprint
from api_token import api_token


url = "https://league-of-legends-esports.p.rapidapi.com/teams"

querystring = {"id":"lng-esports"}

headers = {
	"X-RapidAPI-Key": api_token,
	"X-RapidAPI-Host": "league-of-legends-esports.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)

f = open('response.txt', 'r')
r = f.read()
response = json.loads(r)
pprint.pprint(response)
f.close()