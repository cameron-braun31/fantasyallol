import requests
import json
import pprint


url = "https://league-of-legends-esports.p.rapidapi.com/teams"

querystring = {"id":"lng-esports"}

headers = {
	"X-RapidAPI-Key": "f17f752696mshe5a0346a1f5d235p144ee1jsn119edc9739cb",
	"X-RapidAPI-Host": "league-of-legends-esports.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)

f = open('response.txt', 'r')
r = f.read()
response = json.loads(r)
pprint.pprint(response)
f.close()