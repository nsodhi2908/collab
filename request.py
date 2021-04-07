import os
import urllib
import requests

url = "https://kf.kobotoolbox.org/api/v2/assets/ayYd637KWJhM2eSfAKcjFN/data/?format=geojson"

payload={}
headers = {
  'Authorization': 'Basic a29oYXllOkd1bmp1aWNlNTA5'
}

response = requests.request('GET', url, headers=headers, data=payload)
myfile = open(r"Kobo\geoJSON.geojson", "w")
myfile.write(response.text)
print("done")