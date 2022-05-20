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
    # print(tweet_data)

connection = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO tweets (tweet_id, tweet_text, author_id, conversation_id, created_at, geo_place_id, in_reply_to_user_id, lang, like_count, reply_count, quote_count, retweet_count, possibly_sensitive, reply_settings, source, tweet_url) VALUES \n"

for tweet in tweet_data:

    tweet_id = tweet["id"]
    tweet_text = connection.escape(tweet["text"])
    author_id = connection.escape(tweet["author_id"])
    lang = connection.escape(tweet["lang"])
    created_at = connection.escape(tweet["created_at"])
    like_count = connection.escape(tweet["public_metrics"]["like_count"])
    reply_count = connection.escape(tweet["public_metrics"]["reply_count"])
    quote_count = connection.escape(tweet["public_metrics"]["quote_count"])
    retweet_count = connection.escape(tweet["public_metrics"]["retweet_count"])
    try: 
        geo_place_id = connection.escape(tweet["geo"]["place_id"])
    except: 
        geo_place_id = 'NULL'
    try:
        conversation_id = connection.escape(tweet["conversation_id"])
    except: 
        conversation_id = 'NULL'
    try:
        in_reply_to_user_id = connection.escape(tweet["in_reply_to_user_id"])
    except: 
        in_reply_to_user_id = 'NULL'
    try: 
        possibly_sensitive = connection.escape(tweet["possibly_sensitive"])
    except: 
        possibly_sensitive = 'NULL'
    try:
        reply_settings = connection.escape(tweet["reply_settings"])
    except: 
        reply_settings = 'NULL'
    try:
        source = connection.escape(tweet["source"])
    except: 
        source = 'NULL'
    tweet_url = connection.escape(f"https://twitter.com/twitter/status/{tweet_id}")
    print(tweet_url)
    sql += f"({tweet_id}, {tweet_text}, {author_id}, {conversation_id}, {created_at}, {geo_place_id}, {in_reply_to_user_id}, {lang}, {like_count}, {reply_count}, {quote_count}, {retweet_count}, {possibly_sensitive}, {reply_settings}, {source}, {tweet_url}), \n"

sql = sql[:-3] + ";"
# print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()