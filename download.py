import requests


url = 'https://kf.kobotoolbox.org/private-media/kohaye/exports/Collab_-_all_versions_-_False_-_2021-04-05-15-39-36.geojson'
r = requests.get(url, allow_redirects=True)

open('Kobo/geoJSON.geojson', 'wb').write(r.content)