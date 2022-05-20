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

sql = "REPLACE INTO context_annotations (tweet_id, domain_id, domain_name, domain_description, entity_id, entity_name, entity_description) VALUES \n"

for tweet in tweet_data:
    tweet_id = connection.escape(tweet["id"])
    if "context_annotations" in tweet:
        for anno in tweet["context_annotations"]:
            domain_id = connection.escape(anno["domain"]["id"])
            domain_name = connection.escape(anno["domain"]["name"]) 
            try:
                domain_description = connection.escape(anno["domain"]["description"])
            except:
                domain_description = "NULL"
            entity_id = connection.escape(anno["entity"]["id"])
            entity_name = connection.escape(anno["entity"]["name"]) 
            try:
                entity_description = connection.escape(anno["entity"]["description"])
            except:
                entity_description = "NULL"
            sql += f"({tweet_id}, {domain_id}, {domain_name}, {domain_description}, {entity_id}, {entity_name}, {entity_description}), \n"
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