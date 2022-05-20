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
    user_data = json.load(json_file)["includes"]["users"]

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO users (user_id, name, username, created_at, description, location, pinned_tweet_id, profile_image_url, protected, followers_count, following_count, tweet_count, listed_count, url, verified) VALUES \n"

for user in user_data:

    user_id = connection.escape(user["id"])
    name = connection.escape(user["name"])
    username = connection.escape(user["username"])
    created_at = connection.escape(user["created_at"])
    followers_count = connection.escape(user["public_metrics"]["followers_count"])
    following_count = connection.escape(user["public_metrics"]["following_count"])
    tweet_count = connection.escape(user["public_metrics"]["tweet_count"])
    listed_count = connection.escape(user["public_metrics"]["listed_count"])
    protected = connection.escape(user["protected"])
    verified = connection.escape(user["verified"])
    try:
        pinned_tweet_id = connection.escape(user["pinned_tweet_id"])
    except:
        pinned_tweet_id = 'NULL'
    try:
        description = connection.escape(user["description"])
    except:
        description = 'NULL'
    try:
        location = connection.escape(user["location"])
    except:
        location = 'NULL' 
    try:
        profile_image_url = connection.escape(user["profile_image_url"])
    except:
        profile_image_url = 'NULL'
    try:
        url = connection.escape(user["url"])
    except:
        url = 'NULL'

    sql += f"({user_id}, {name}, {username}, {created_at}, {description}, {location}, {pinned_tweet_id}, {profile_image_url}, {protected}, {followers_count}, {following_count}, {tweet_count}, {listed_count}, {url}, {verified}), \n"

sql = sql[:-3] + ";"
print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()