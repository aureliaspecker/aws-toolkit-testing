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

sql = "REPLACE INTO attachments_media (tweet_id, media_key) VALUES \n"

for tweet in tweet_data:
    tweet_id = tweet["id"]
    if "attachments" in tweet:
        print(tweet["attachments"])
        if "media_keys" in tweet["attachments"]: 
            count = 0
            for key in tweet["attachments"]["media_keys"]:
                media_key = connection.escape(tweet["attachments"]["media_keys"][count])
                sql += f"({tweet_id}, {media_key}), \n"
                count += 1
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