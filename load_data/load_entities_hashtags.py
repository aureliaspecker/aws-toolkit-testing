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

sql = "REPLACE INTO entities_hashtags (tweet_id, start, end, hashtag) VALUES \n"

for tweet in tweet_data:
    tweet_id = connection.escape(tweet["id"])
    if "entities" in tweet:
        if "hashtags" in tweet["entities"]:
            for hashtg in tweet["entities"]["hashtags"]:
                start =  connection.escape(hashtg["start"])
                end = connection.escape(hashtg["end"])
                hashtag = connection.escape(hashtg["tag"])
                sql += f"({tweet_id}, {start}, {end}, {hashtag}), \n"
        else:
            pass
    else: 
        pass

sql = sql[:-3] + ";"
# print(sql.count)
# print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()