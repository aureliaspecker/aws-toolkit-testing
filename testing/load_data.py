
import json
import pymysql

# Replace details below, between quotation marks 
ENDPOINT=""
USER=""
REGION=""
DBNAME=""

# Replace file name details below
with open('payload-1-20220424153627.json') as json_file:
    tweet_data = json.load(json_file)["data"]
    # print(tweet_data)

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd="Test1230", db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO tweets (id, tweet_text, author_id, conversation_id, created_at, in_reply_to_user_id, lang, like_count, reply_count, quote_count, retweet_count, possibly_sensitive, reply_settings, source, tweet_url) VALUES \n"

for tweet in tweet_data:

    id = connection.escape(tweet["id"])
    tweet_text = connection.escape(tweet["text"])
    author_id = connection.escape(tweet["author_id"])
    lang = connection.escape(tweet["lang"])
    created_at = connection.escape(tweet["created_at"])
    like_count = connection.escape(tweet["public_metrics"]["like_count"])
    reply_count = connection.escape(tweet["public_metrics"]["reply_count"])
    quote_count = connection.escape(tweet["public_metrics"]["quote_count"])
    retweet_count = connection.escape(tweet["public_metrics"]["retweet_count"])
    try:
        conversation_id = connection.escape(tweet["conversation_id"])
    except: 
        conversation_id = 'NULL'
    try:
        in_reply_to_user_id = connection.escape(tweet["in_reply_to_user_id"])
    except: 
        in_reply_to_user_id = 'NULL'
    try: 
        possibly_sensitive = connection.escape(tweet["possibly_sensitive"])
    except: 
        possibly_sensitive = 'NULL'
    try:
        reply_settings = connection.escape(tweet["reply_settings"])
    except: 
        reply_settings = 'NULL'
    try:
        source = connection.escape(tweet["source"])
    except: 
        source = 'NULL'
    tweet_url = connection.escape(f"https://twitter.com/twitter/status/{id}")
    print(tweet_url)
    sql += f"({id}, {tweet_text}, {author_id}, {conversation_id}, {created_at}, {in_reply_to_user_id}, {lang}, {like_count}, {reply_count}, {quote_count}, {retweet_count}, {possibly_sensitive}, {reply_settings}, {source}, {tweet_url}), \n"

sql = sql[:-3] + ";"
print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()