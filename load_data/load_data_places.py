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
    place_data = json.load(json_file)["includes"]["places"]

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO places (place_id, full_name, country, country_code, name, place_type) VALUES \n"

for place in place_data:

    place_id = connection.escape(place["id"])
    full_name = connection.escape(place["full_name"])
    try:
        country = connection.escape(place["country"])
    except:
        country = 'NULL'
    try: 
        country_code = connection.escape(place["country_code"])
    except:
        country_code = 'NULL'
    try: 
        name = connection.escape(place["name"])
    except:
        name = 'NULL'
    try: 
        place_type = connection.escape(place["place_type"])
    except:
        place_data = 'NULL'

    sql += f"({place_id}, {full_name}, {country}, {country_code}, {name}, {place_type}), \n"

sql = sql[:-3] + ";"
print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()