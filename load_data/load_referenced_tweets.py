import json
import pymysql
import os

from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

ENDPOINT=os.getenv("endpoint")
USER=os.getenv("user")
REGION=os.getenv("region")
DBNAME=os.getenv("dbname")
PASSWORD=os.getenv("password")
FILENAME = os.getenv("filename")

with open(FILENAME) as json_file:
    tweet_data = json.load(json_file)["data"]

connection = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO referenced_tweets (tweet_id, referenced_tweet_type, referenced_tweet_id) VALUES \n"

for tweet in tweet_data:
    tweet_id = tweet["id"]
    if "referenced_tweets" in tweet: 
        referenced_tweets = tweet["referenced_tweets"]
        for ref_tweet in referenced_tweets: 
            referenced_tweet_type = connection.escape(ref_tweet["type"])
            referenced_tweet_id = connection.escape(ref_tweet["id"])
            sql += f"({tweet_id}, {referenced_tweet_type}, {referenced_tweet_id}), \n"
    else:
        pass

sql = sql[:-3] + ";"
print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()