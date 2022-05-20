from cmath import exp
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

sql = "REPLACE INTO entities_urls (tweet_id, start, end, url, expanded_url, display_url, status, title, description, unwound_url) VALUES \n"

for tweet in tweet_data:
    tweet_id = connection.escape(tweet["id"])
    if "entities" in tweet:
        if "urls" in tweet["entities"]:
            for u in tweet["entities"]["urls"]:
                start =  connection.escape(u["start"])
                end = connection.escape(u["end"])
                url = connection.escape(u["url"])
                try:
                    expanded_url = connection.escape(u["expanded_url"])
                except: 
                    expanded_url = "NULL"
                try:
                    display_url = connection.escape(u["display_url"])
                except:
                    display_url = "NULL"
                try:
                    status = connection.escape(u["status"])
                except:
                    status = "NULL"
                try: 
                    title = connection.escape(u["title"])
                except:
                    title = "NULL"
                try: 
                    description = connection.escape(u["description"])
                except: 
                    description = "NULL"
                try: 
                    unwound_url = connection.escape(u["unwound_url"])
                except: 
                    unwound_url = "NULL"
                sql += f"({tweet_id}, {start}, {end}, {url}, {expanded_url}, {display_url}, {status}, {title}, {description}, {unwound_url}), \n"
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