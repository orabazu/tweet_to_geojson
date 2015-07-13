import json
import pprint
import geojson
from geojson import Feature, Point, FeatureCollection
data = []
geoms = []
tweet_features = []
with open('raw.json') as twtr_hamdata:    
    for satir in twtr_hamdata:
        data.append(json.loads(satir))

for i in range(0,len(data)):
    geoms.append(data[i]["geo"]["coordinates"])
    print geoms[i][0], geoms[i][1]
    my_feature = Feature(geometry=Point((float(geoms[i][1]),float(geoms[i][0]))),\
    properties={"user_location":data[i]["user"]["location"],\
    "user_id": data[i]["id"],\
    "user_name":data[i]["user"]["name"],\
    "screen_name":data[i]["user"]["screen_name"],\
    "followers_count":data[i]["user"]["followers_count"],\
    "tweet":data[i]["text"],\
    "tweet_time":data[i]["created_at"]})
    tweet_features.append(my_feature)
	#print tweet_features
tweet_FeatureCollection = FeatureCollection(tweet_features[:])
#print tweet_FeatureCollection["type"]
try:
    saveFile = open('tweets.geojson','a')
    saveFile.write(json.dumps(tweet_FeatureCollection))
    saveFile.close()
except Exception as error:
    print "Unable to write %s error"%error