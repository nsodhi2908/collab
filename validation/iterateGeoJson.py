import geojson, json
from shapely.geometry import shape, point
from shapely.geometry.point import Point
geoPoints = open(r"validation\geoJSON.geojson", "r")
criteriaPoints = open(r"validation\polygon.geojson", "r")
geodict = json.load(geoPoints)
criteriadict = json.load(criteriaPoints)
resultPoints = open(r"validation\result.geojson", "w")
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
for feat in geodict["features"]:
    print(feat["geometry"]["coordinates"])
    myPoint = feat["geometry"]["coordinates"]
    for feature in criteriadict["features"]:
        polygon = shape(feature["geometry"])
        if polygon.contains(Point(myPoint)):
            feature_collection["features"].append(feat)
            print(feat["geometry"]["coordinates"])
        # geojson.dump(feat, resultPoints)
        # # resultPoints.append(feat) --> did not work
    # for points in feat["geometry"]:
    #     print (feat["geometry"]["coordinates"])
# import geojson
# with open(r"Kobo\geoJSON.geojson") as f:
#     gj = geojson.load(f)
# features = gj['features'][0]
# print(features)
geojson.dump(feature_collection, resultPoints)