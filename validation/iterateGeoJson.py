import geojson, json
geoPoints = open(r"validation\geoJSON.geojson", "r")
geodict = json.load(geoPoints)
for feat in geodict["features"]:
    print(feat["geometry"]["coordinates"])
    # for points in feat["geometry"]:
    #     print (feat["geometry"]["coordinates"])
# import geojson
# with open(r"Kobo\geoJSON.geojson") as f:
#     gj = geojson.load(f)
# features = gj['features'][0]
# print(features)