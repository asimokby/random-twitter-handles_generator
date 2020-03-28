# Random Twitter Handles Generator
**Random handles are generated based on:**
* country name
* specified number of random coordinate points in that country
* radius of the given latitude/longitude(coordinate point) in km (tweets will be within that radius)
* specified number of tweets to get per a coordinate point
* language of the tweets

### Setup
- First, you need to have a twitter [developer account](https://developer.twitter.com/en/apply-for-access). Create one if you do not already, then create an app to get your credentials: 
    * ACCESS_TOKEN = "" 
    * ACCESS_TOKEN_SECRET = ""
    * CONSUMER_KEY = ""
    * CONSUMER_SECRET = ""

- Then you need to install a couple of packages:
```
$ pip install tweepy
$ pip install PyCristoforo
```
### Usage

* Fill in your credentials in the **randHandles.py** file in the specified place inside **authorization** method. 
* Run example.py after setting up your environment*. You should get a file called **turkeyHandles.txt** that contains the **randomly generated twitter handles**.
```
countries = ['Turkey']   
langs = ['tr']
fileNames = ['turkeyHandles.txt'] 
for i in range(len(countries)):         
    randHandles = RandHandles(countries[i], 10, 100, 5, langs[i], fileNames[i])
    randHandles.getHandles()
```
