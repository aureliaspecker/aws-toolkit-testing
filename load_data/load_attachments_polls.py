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

sql = "REPLACE INTO attachments_polls (tweet_id, poll_id) VALUES \n"

for tweet in tweet_data:
    tweet_id = tweet["id"]
    if "attachments" in tweet:
        print(tweet["attachments"])
        if "poll_ids" in tweet["attachments"]: 
            poll_id = connection.escape(tweet["attachments"]["poll_ids"])
            print(poll_id[0])
            sql += f"({tweet_id}, {poll_id}), \n"
        else:
            pass
    else: 
        pass

sql = sql[:-3] + ";"
print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()