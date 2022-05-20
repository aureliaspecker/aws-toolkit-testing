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
    media_data = json.load(json_file)["includes"]["media"]

connection = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO media (media_key, type, url, duration_ms, height, preview_image_url, view_count, width, alt_text) VALUES \n"

for media in media_data:

    media_key = connection.escape(media["media_key"])
    type = connection.escape(media["type"])
    try:
        url = connection.escape(media["url"])
    except: 
        url = 'NULL'
    try:
        duration_ms = connection.escape(media["duration_ms"])
    except: 
        duration_ms = 'NULL'
    try: 
        height = connection.escape(media["height"])
    except:
        height = 'NULL'
    try: 
        preview_image_url = connection.escape(media["preview_image_url"])
    except:
        preview_image_url = 'NULL'
    try: 
        view_count = connection.escape(media["public_metrics"]["view_count"])
    except: 
        view_count = 'NULL'
    try: 
        width = connection.escape(media["width"])
    except:
        width = 'NULL'
    try:
        alt_text = connection.escape(media["alt_text"])
    except:
        alt_text = 'NULL'

    sql += f"({media_key}, {type}, {url}, {duration_ms}, {height}, {preview_image_url}, {view_count}, {width}, {alt_text}), \n"

sql = sql[:-3] + ";"
print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()