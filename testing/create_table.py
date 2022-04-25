import pymysql

# Replace details below, between quotation marks 
ENDPOINT=""
USER=""
REGION=""
DBNAME=""

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd="", db=DBNAME)
cursor = connection.cursor()

sql_query = "CREATE table tweets (id VARCHAR(50) NOT NULL, tweet_text VARCHAR(280) NOT NULL, PRIMARY KEY (id))"

cursor.execute(sql_query)
connection.commit()

connection.close()