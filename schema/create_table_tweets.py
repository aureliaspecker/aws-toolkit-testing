import pymysql
import os

from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

ENDPOINT=os.getenv("endpoint")
USER=os.getenv("user")
REGION=os.getenv("region")
DBNAME=os.getenv("dbname")
PASSWORD=os.getenv("password")

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, db=DBNAME)
cursor = connection.cursor()

sql_query = "CREATE table tweets (tweet_id VARCHAR(50) NOT NULL, tweet_text VARCHAR(280) NOT NULL, author_id VARCHAR(50), conversation_id VARCHAR(50), created_at DATETIME, geo_place_id VARCHAR(50), in_reply_to_user_id VARCHAR(50), lang VARCHAR(10), like_count INT, reply_count INT, quote_count INT, retweet_count INT, possibly_sensitive VARCHAR(10), reply_settings VARCHAR(20), source VARCHAR(100), tweet_url VARCHAR(100), PRIMARY KEY (tweet_id))"

cursor.execute(sql_query)
connection.commit()

connection.close()