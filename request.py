import requests

import geojson, json
from shapely.geometry import shape
from shapely.geometry.point import Point

url = "https://kobo.humanitarianresponse.info/api/v2/assets//anpv3H2CEtV6PzAcyfDgE6/data/?format=geojson"

payload={}
headers = {
  'Authorization': 'Basic ZnJ1aXR0cmVlbWFwOkZvb2RTZWN1cml0eTIwMjE='
}

response = requests.request('GET', url, headers=headers, data=payload)
myfile = open(r"validation\kobo.geojson", "w")
myfile.write(response.text)
myfile.close()
print("done")




#########################################################################
purl = "https://github.com/nsodhi2908/collab/raw/a2acedf583049b995e507b7babd494c0fc4ef94a/polygon.geojson"
criteriaPoints = requests.request('GET', purl, data=payload)
cp = criteriaPoints.text
rurl = "https://github.com/nsodhi2908/collab/raw/a2acedf583049b995e507b7babd494c0fc4ef94a/polygonMinusWater.geojson"
regionPoints = requests.request('GET', rurl, data=payload)
rp = regionPoints.text
badtrees = ["garbage", "Garbage", "Dumpster", "dumpster", "Buckthorn", "Buck Thorn", "Oak", "buckthorn", "buck thorn", "poison", "Poison", "Sumac", "sumac", "Blue Beech", "blue beech"]
geoPoints = open(r"validation\kobo.geojson", "r")
# criteriaPoints = open(r"https://github.com/nsodhi2908/collab/raw/a2acedf583049b995e507b7babd494c0fc4ef94a/polygon.geojson", "r")
# regionPoints = open(r"https://github.com/nsodhi2908/collab/raw/a2acedf583049b995e507b7babd494c0fc4ef94a/polygonMinusWater.geojson", "r")
geodict = json.load(geoPoints)
criteriadict = json.load(cp)
regiondict = json.load(rp)
resultPoints = open(r"validation\result.geojson", "w")

feature_collection = {"type": "FeatureCollection",
                      "name": "Collab",
                      "features": []
                      }

for feat in geodict["features"]:
    myPoint = feat["geometry"]["coordinates"]
    if feat["properties"]["Species"] == "Other":
      for i in badtrees:
        if i not in feat["properties"]["OtherTreeName"]:
          if feat["properties"]["Public"] == "Uknown":
            for feature in criteriadict["features"]:
              polygon = shape(feature["geometry"])
              if polygon.contains(Point(myPoint)):
                feature_collection["features"].append(feat)
          else:
            for feature in regiondict["features"]:
              polygon = shape(feature["geometry"])
              if polygon.contains(Point(myPoint)):
                feature_collection["features"].append(feat)

    if feat["properties"]["Public"] == "Uknown":
      for feature in criteriadict["features"]:
          polygon = shape(feature["geometry"])
          if polygon.contains(Point(myPoint)):
              feature_collection["features"].append(feat)
    else:
      for feature in regiondict["features"]:
        polygon = shape(feature["geometry"])
        if polygon.contains(Point(myPoint)):
          feature_collection["features"].append(feat)

geojson.dump(feature_collection, resultPoints)
print("done")
