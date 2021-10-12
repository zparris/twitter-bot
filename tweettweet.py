import time

import tweepy

auth = tweepy.OAuthHandler('x6el7jZEk9kZdFaZJdZJ1GDwi', 'gu5Ac3OO2nlj9KIa4qULMPphpr9ZknOxBUKbpTEiUoxldBUdOX')
auth.set_access_token('2362549385-SdoZ6993XAm48MB4ruhilVmyqE1M2mr9VPgTBok', '8FAnTTAI9x7tbj8wv0anqKke0EZYcTtzIcpMtkpb9KfEd')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
        	yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1)


search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
	try:
		tweet.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
