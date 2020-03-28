from randCoordinates import randCoordinatesGenerator
import tweepy as tw

class RandHandles():
    """  
    Random handles are generated given:
        - country name, 
        - specified number of random coordinate points in that country,
        - radius of the given latitude/longitude(coordinate point) in km, 
        - specified number of tweets to get per a coordinate point,
        - language of the tweets,
    The are saved in a given filename: the default is 'output.txt'
    """
    def __init__(self, country_name, numRandCoordinates, radiusOfCoordinate, numTweetsPerCoordinate, tweetsLang, fileName='output.txt'):
        self.radiusOfCoordinate = radiusOfCoordinate 
        self.numTweetsPerCoordinate = numTweetsPerCoordinate 
        self.country_name = country_name
        self.numRandCoordinates = numRandCoordinates
        self.tweetsLang = tweetsLang
        self.fileName = fileName
        self.auth = self.authorization()
        randGen = randCoordinatesGenerator(self.country_name, self.numRandCoordinates)
        self.points = randGen.points

    def authorization(self): 
        """ returns an auth for calling the API """
        ACCESS_TOKEN = ""
        ACCESS_TOKEN_SECRET = ""
        CONSUMER_KEY = ""
        CONSUMER_SECRET = ""

        if len(ACCESS_TOKEN.strip()) == 0:
            raise ValueError('Please, provide your auth information')
        # Authorization to consumer key and consumer secret 
        auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
        # Access to user's access key and access secret 
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 
        return auth 

    def get_tweets(self, q, lang, geo, numTweets): 
        """ 
        this method gets specified number of tweets based on geo
        coordinates,query, and language. Then saves them all to a text file given its name
        """	
        # Calling api 
        api = tw.API(self.auth, wait_on_rate_limit=True) 
        tweets = tw.Cursor(api.search,q=q,lang=lang,geocode=geo,exclude_replies=True,wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items(numTweets)
       
        self.saveTweets(tweets, self.fileName)


    def saveTweets(self, tweets, fileName):
        """ this method saves all usernames of
         the random tweets in a txt file """
        with open(fileName, 'a') as f:
            for tweet in tweets:
                username = tweet._json['user']['screen_name'] 
                f.write(username)
                f.write('\n')

    def getHandles(self):
        """ 
        this method gets the specified number of tweets in a specific lang
        for each random coordinate while considering the radius in km. 
        """
        for point in self.points: 
            geo = f'{point[0]},{point[1]},{self.radiusOfCoordinate}km'
            self.get_tweets(' ', self.tweetsLang, geo, self.numTweetsPerCoordinate)  
        print(f'Handles are saved in {self.fileName}')
    



