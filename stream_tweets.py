from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey='<your ckey>'
csecret='<your csecret>'
atoken='<auth key>'
asecret='<auth secret>'
data_json = {}

class listener(StreamListener):

    def on_data(self,data):
        data_json = json.loads(data)
        #check if user is sharing precise location
        try:
            _location = data_json['geo']
            saveFile = open('raw.json','a')
        
            if _location == None:
                print ':(   User %s is not sharing location'%data_json['user']['screen_name']
                saveFile.close()
            else:
                saveFile.write(data)
                saveFile.close()
                print ':)   You got one !'
                print ' %s tweet is written @%s' %(data_json['user']['screen_name'],data_json['geo']['coordinates'])

            data_json = {}
            return True
        except:
            pass
        
    def on_error(self,status):
        print status
        
auth= OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["here"])
