import pymysql

# Replace details below, between quotation marks 
ENDPOINT=""
USER=""
REGION=""
DBNAME=""

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd="", db=DBNAME)
cursor = connection.cursor()

sql_context_annotations = "CREATE table context_annotations (tweet_id VARCHAR(50) NOT NULL, domain_id VARCHAR(50), domain_name VARCHAR(50), domain_description VARCHAR(200), entity_id VARCHAR(50), entity_name VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_entities_annotations = "CREATE table entities_annotations (tweet_id VARCHAR(50) NOT NULL, start INT, end INT, probability INT, type VARCHAR(20), normalized_text VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_entities_cashtags = "CREATE table entities_cashtags (tweet_id VARCHAR (50) NOT NULL, start INT, end INT, cashtag VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_entities_hashtags = "CREATE table entities_hashtags (tweet_id VARCHAR (50) NOT NULL, start INT, end INT, hashtag VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_entities_mentions = "CREATE table entities_mentions (tweet_id VARCHAR (50) NOT NULL, start INT, end INT, mention VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_entities_urls = "CREATE table entities_urls (tweet_id VARCHAR(50) NOT NULL, start INT, end INT, url VARCHAR(100), expanded_url VARCHAR(200), display_url VARCHAR(200), status VARCHAR(50), title VARCHAR(200), description VARCHAR(500), unwound_url VARCHAR(500), PRIMARY KEY (tweet_id))"

sql_referenced_tweets = "CREATE table referenced_tweets (tweet_id VARCHAR(50) NOT NULL, referenced_tweet_type VARCHAR(50), referenced_tweet_id VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_users = "CREATE table users(user_id VARCHAR(50) NOT NULL, name VARCHAR(100) NOT NULL, username VARCHAR(50) NOT NULL, created_at DATETIME, description VARCHAR(300), location VARCHAR(200), pinned_tweet_id VARCHAR(50), profile_image_url VARCHAR(300), protected VARCHAR(20), followers_count INT, following_count INT, tweet_count INT, listed_count INT, url VARCHAR(200), verified VARCHAR(20), PRIMARY KEY (user_id))"

sql_attachments_polls = "CREATE table attachments_polls(tweet_id VARCHAR(50) NOT NULL, poll_id VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_attachments_media = "CREATE table attachments_media(tweet_id VARCHAR(50) NOT NULL, media_key VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_polls = "CREATE table polls(poll_id VARCHAR(50) NOT NULL, option_1 VARCHAR(100) NOT NULL, option_2 VARCHAR(200) NOT NULL, option_3 VARCHAR(200), option_4 VARCHAR(200), duration_minutes INT, end_datetime DATETIME, PRIMARY KEY (poll_id))"

sql_media = "CREATE table media(media_key VARCHAR(50) NOT NULL, type VARCHAR(50) NOT NULL, url VARCHAR(300), duration_ms INT, height INT, preview_image_url VARCHAR(300), view_count INT, width INT, alt_text VARCHAR(300), PRIMARY KEY (media_key))"

sql_place = "CREATE table place(place_id VARCHAR(50) NOT NULL, full_name VARCHAR(200) NOT NULL, country VARCHAR(200), country_code VARCHAR(20), name VARCHAR(200), place_type VARCHAR(50), PRIMARY KEY (place_id))"

cursor.execute(sql_context_annotations)

cursor.execute(sql_entities_annotations)

cursor.execute(sql_entities_cashtags)

cursor.execute(sql_entities_hashtags)

cursor.execute(sql_entities_mentions)

cursor.execute(sql_entities_urls)

cursor.execute(sql_referenced_tweets)

cursor.execute(sql_users)

cursor.execute(sql_attachments_polls)

cursor.execute(sql_attachments_media)

cursor.execute(sql_polls)

cursor.execute(sql_media)

cursor.execute(sql_place)

connection.commit()

connection.close()