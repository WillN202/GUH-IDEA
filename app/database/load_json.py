from models.company import Company
from models.tweet import Tweet
from datetime import date, datetime
import json
import uuid

DATABASE_FILE = "C:/Users/Willi/Downloads/GUH_APP/app/database/data.json"

def parse_tweets(tweets):
    print(tweets)
    processed_tweets = []
    for tweet in tweets:
        id_num = str(uuid.uuid4())[0:16]
        body = tweet["content"]
        retweets = tweet["retweets"]
        quote_tweets = tweet["quote_tweets"]
        likes = tweet["likes"]
        date = datetime.strptime(tweet["date_posted"], "%I:%M %p %d %b %Y")
        vibes = "" if tweet.get("vibes", None) is None else tweet["vibes"]
        attachment = "" if tweet.get("attachment", None) is None else tweet["attachment"]
        
        new_tweet = Tweet(id_num=id_num, body=body, retweets=retweets, quote_tweets=quote_tweets, likes=likes, date=date, vibe=vibes, attachment=attachment)
        processed_tweets.append(new_tweet)
    
    return processed_tweets
        

def load_data():
    content = open(DATABASE_FILE, "rt")
    database_data = json.loads(content.read())
    companies_list = []

    for company in database_data["companies"]:
        ids = str(uuid.uuid4())[0:16]
        handle = company["account_handle"]
        picture = None if company.get("account_picture", None) is None else company["account_picture"]
        name = company["account_name"]
        followers = company["followers"]
        following = company["following"]
        date = datetime.strptime(company["joined_date"], "%B %Y")
        real_tweets = parse_tweets(company["real_tweets"])
        fake_tweets = parse_tweets(company["fake_tweets"])

        new_company = Company(id=ids, name=name, handle=handle, picture=picture, followers=followers, following=following, 
            joined_date=date, correct_tweets = real_tweets, incorrect_tweets=fake_tweets)

        companies_list.append(new_company)
    
    return companies_list



    
