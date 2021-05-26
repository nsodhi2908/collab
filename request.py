import requests

import geojson, json
from shapely.geometry import shape
from shapely.geometry.point import Point

# url = "https://kf.kobotoolbox.org/api/v2/assets/ayYd637KWJhM2eSfAKcjFN/data/?format=geojson"

# payload={}
# headers = {
#   'Authorization': 'Basic a29oYXllOkd1bmp1aWNlNTA5'
# }

# response = requests.request('GET', url, headers=headers, data=payload)
# myfile = open(r"Kobo\geoJSON.geojson", "w")
# myfile.write(response.text)
# print("done")


#########################################################################

geoPoints = open(r"validation\TestData_May26.geojson", "r")
criteriaPoints = open(r"validation\polygon.geojson", "r")
geodict = json.load(geoPoints)
criteriadict = json.load(criteriaPoints)
resultPoints = open(r"validation\result.geojson", "w")

feature_collection = {"type": "FeatureCollection",
                      "name": "Collab",
                      "features": []
                      }

for feat in geodict["features"]:
    myPoint = feat["geometry"]["coordinates"]
    if feat["properties"]["Public"] == "Uknown":
      for feature in criteriadict["features"]:
          polygon = shape(feature["geometry"])
          if polygon.contains(Point(myPoint)):
              feature_collection["features"].append(feat)
    else: feature_collection["features"].append(feat)

geojson.dump(feature_collection, resultPoints)
print("done")