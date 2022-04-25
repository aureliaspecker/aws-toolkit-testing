# This script was used to test S3 and RDS functionality. 
# The code below gets 

import boto3
import json
import pymysql

s3 = boto3.client('s3')
rds = boto3.client('rds')

bucket = "search-tweets"
key = "payload-2-20220424153628.json" #Change to variable.

# Replace details below, between quotation marks 
ENDPOINT=""
USER=""
REGION=""
DBNAME=""

response = s3.get_object(Bucket=bucket, Key=key)
response_decode = response["Body"].read().decode("utf-8")
tweet_data = json.loads(response_decode)["data"]
# print(type(tweet_data))
# print(tweet_data)

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd="", db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO tweets ( id, tweet_text ) VALUES \n"

for tweet in tweet_data:
    id = connection.escape(tweet["id"])
    text = connection.escape(tweet["text"])
    sql += f"({id}, {text}), \n"

sql = sql[:-3] + ";"
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()