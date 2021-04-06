import requests


url = 'https://kf.kobotoolbox.org/api/v2/assets/ayYd637KWJhM2eSfAKcjFN/data/?format=json'
r = requests.get(url, allow_redirects=True)

open('Kobo/geoJSON.geojson', 'wb').write(r.content)