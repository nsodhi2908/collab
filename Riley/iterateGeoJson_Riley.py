import geojson, json
from shapely.geometry import shape, Point
geoPoints = open(r"validation\geoJSON.geojson", "r")
geodict = json.load(geoPoints)
resultPoints = open(r"Riley\Output.geojson", "w")
# geoHeader = [ '{', '"', 'type','"',':', '"','FeatureCollection','"', ',' , '"', 'name' , '"', ':',  '"', 'Collab', '"', ',', '"', 'features', '"', ':',  '[' ]

feature_collection = {"type": "FeatureCollection",
                      "name": "Collab",
                      "features": []
                      }

# feature_collection["features"].append(feat)
# for i in geoHeader:
#    #code to generate your geoJSON
#    geo_json_list.append(resultPoints)
    # geojson.dump(i, resultPoints)

#for feature in js['features']:
    #polygon = shape(feature['geometry'])
    #if polygon.contains(point):
        #print 'Found containing polygon:', feature



criteriaPoints = open(r"validation\Criteria.geojson", "r")
geodict2 = json.load(criteriaPoints)


for marker in geodict["features"]:
   point = shape(feature['geometry'])
   for feat in geodict2["features"]:
      criteria = shape(feature['geometry'])
      if criteria.contains(point):
         print("true")

##Testing with feature collection polygon, and random point.
#geojson = """{"type":"Point","coordinates":[108420.33,753808.59]}"""
# criteria = {
#   "type": "FeatureCollection",
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#           [
#             [
#               -79.51904296874999,
#               44.03232064275081
#             ],
#             [
#               -79.53140258789062,
#               43.94438361223957
#             ],
#             [
#               -79.354248046875,
#               43.9473499035071
#             ],
#             [
#               -79.37072753906249,
#               44.03034596066819
#             ],
#             [
#               -79.51904296874999,
#               44.03232064275081
#             ]
#           ]
#         ]
#       }
#     }
#   ]
# }

# for feature in criteria['features']:
#     polygon = shape(feature['geometry'])
#     if polygon.contains(geojson):
#         print("True")

# for feat in geodict2["features"]:
#    criteria = shape(feature['geometry'])
#    if criteria.contains(geojson):
#       print("true")

# for point in geodict["features"]:
#    for feat in geodict2["features"]:
#       criteria = shape(feature['geometry'])
#       if criteria.contains(point):
#          print("true")
#for feat in geodict["features"]:
  # if criteriaPoints.contains(feat):
     # print("true")


    #print(feat["geometry"]["coordinates"])
    #if True == True:
        #feature_collection["features"].append(feat)
        # geojson.dump(feat, resultPoints)
        # # resultPoints.append(feat) --> did not work
    # for points in feat["geometry"]:
    #     print (feat["geometry"]["coordinates"])
# import geojson
# with open(r"Kobo\geoJSON.geojson") as f:
#     gj = geojson.load(f)
# features = gj['features'][0]
# print(features)
#geojson.dump(feature_collection, resultPoints)