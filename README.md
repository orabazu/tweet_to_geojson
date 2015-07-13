# Tweet to GeoJSON
Bunch of code let you stream twitter data with a given hashtag or keyword then convert it to proper GeoJSON format.
![Alt text](http://i.imgur.com/15slne0.jpg"title")
### Version
0.0.1

### Dependencies
Dependencies can be downloaded by *requirements.txt* with [pip] 
* [tweepy]
* [geojson]

#### Windows
    cd <directory>
    python -m pip install -r requirements.txt

### Usage
Get your Consumer Key and Consumer Secret key
    
    ckey='<your_ckey>'
    csecret='<your_csecret>'
    atoken='<your_authtoken>'
    asecret='<your_authsecret>'
[How to get key] 

Set hashtag or keyword to listen stream

    twitterStream.filter(track=["here"])
    
Run livestream

    python stream_tweets.py
    # out: raw.json
    
Stop live stream than process raw twitter data

    python tweet_to_geojson.py
    # out: tweets.geojson
### Development
Contribute anyway you like

### Data Visualization
The [QGIS] is an oldschool way by loading *tweets.geojson*  (example above) or just matplotlib [basemap] toolkit 


### Todo's
example Gist with leaflet.js and geojson layer


License
----

MIT

[basemap]:http://matplotlib.org/basemap/index.html
[tweepy]:http://www.tweepy.org/
[geojson]:https://pypi.python.org/pypi/geojson/
[pip]:https://pypi.python.org/pypi
[how to get key]:http://support.yapsody.com/hc/en-us/articles/203068116-How-do-I-get-a-Twitter-Consumer-Key-and-Consumer-Secret-key-
[QGIS]:http://www.qgis.org/en/site/

