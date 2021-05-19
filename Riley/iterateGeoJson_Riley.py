import geojson, json
geoPoints = open(r"validation\geoJSON.geojson", "r")
geodict = json.load(geoPoints)
resultPoints = open(r"Riley\Output.geojson", "w")

for feat in geodict["features"]:
    print(feat["geometry"]["coordinates"])
#geoEnder = "]}"
#geo_json_list = []
#for i in geoEnder:
   #code to generate your geoJSON
   geo_json_list.append(i)
#with open(resultPoints, 'a') as f:
   #json.dump(geo_json_list, f)



#for feat in geodict["features"]:
   # print(feat["geometry"]["coordinates"])
    # for points in feat["geometry"]:
    #     print (feat["geometry"]["coordinates"])
# import geojson
# with open(r"Kobo\geoJSON.geojson") as f:
#     gj = geojson.load(f)
# features = gj['features'][0]
# print(features)
