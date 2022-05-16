import pymysql

# Replace details below, between quotation marks 
ENDPOINT=""
USER=""
REGION=""
DBNAME=""

# Insert password below, between quotation marks
connection = pymysql.connect(host=ENDPOINT, user=USER, passwd="", db=DBNAME)
cursor = connection.cursor()

sql_twitter_users = "CREATE table twitter_users (tweet_id VARCHAR(50) NOT NULL, user_id VARCHAR(50) NOT NULL, name VARCHAR(100) NOT NULL, username VARCHAR(50) NOT NULL, created_at DATETIME, description VARCHAR(200), location VARCHAR(200), pinned_tweet_id VARCHAR(50), profile_image_url VARCHAR(200), protected VARCHAR(10), followers_count INT, following_count INT, tweet_count INT, listed_count INT, likes_count INT, statuses_count INT, url VARCHAR(200), verified VARCHAR(10), PRIMARY KEY (tweet_id))"

sql_context_annotations = "CREATE table context_annotations (tweet_id VARCHAR(50) NOT NULL, domain_id VARCHAR(50), domain_name VARCHAR(50), domain_description VARCHAR(200), entity_id INT, entity_name VARCHAR(50), entity_description VARCHAR(200), PRIMARY KEY (tweet_id))"

sql_hashtags = "CREATE table hashtags (tweet_id VARCHAR(50) NOT NULL, hashtag VARCHAR(280) NOT NULL, PRIMARY KEY (tweet_id))"

sql_cashtags = "CREATE table cashtags (tweet_id VARCHAR(50) NOT NULL, cashtag VARCHAR(100) NOT NULL, PRIMARY KEY (tweet_id))"

sql_urls = "CREATE table urls (tweet_id VARCHAR(50) NOT NULL, display_url VARCHAR(280), PRIMARY KEY (tweet_id))" 

sql_mentions = "CREATE table mentions (tweet_id VARCHAR(50) NOT NULL, mentioned_user_id VARCHAR(50) NOT NULL, mentioned_user_name VARCHAR(100) NOT NULL, mentioned_user_username VARCHAR(50) NOT NULL, PRIMARY KEY (tweet_id))"

sql_media = "CREATE table media (tweet_id VARCHAR(50) NOT NULL, display_url VARCHAR(280), media_url VARCHAR(280), media_type VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_extended_entities = "CREATE table extended_entities (tweet_id VARCHAR(50) NOT NULL, display_url VARCHAR(280), media_url VARCHAR(280), media_type VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_polls = "CREATE table polls (tweet_id VARCHAR(50) NOT NULL, option_text VARCHAR(150), end_time VARCHAR(100), duration_minutes VARCHAR(50), PRIMARY KEY (tweet_id))"

sql_places = "CREATE table places (tweet_id VARCHAR(50) NOT NULL, place_id VARCHAR(50), place_url VARCHAR(100), place_type VARCHAR(50), place_name VARCHAR(50), place_full_name VARCHAR(100), place_country_code VARCHAR(50), place_country VARCHAR(100), PRIMARY KEY (tweet_id))" #needs finishing

sql_derived_locations = "CREATE table derived_locations (tweet_id VARCHAR(50) NOT NULL, derived_country VARCHAR(50), derived_country_code VARCHAR(20), derived_locality VARCHAR(100), derived_region VARCHAR(100), derived_full_name VARCHAR(150), PRIMARY KEY (tweet_id))"

cursor.execute(sql_twitter_users)

cursor.execute(sql_context_annotations)

cursor.execute(sql_hashtags)

cursor.execute(sql_cashtags)

cursor.execute(sql_urls)

cursor.execute(sql_mentions)

cursor.execute(sql_media)

cursor.execute(sql_extended_entities)

cursor.execute(sql_polls)

cursor.execute(sql_places)

cursor.execute(sql_derived_locations)

connection.close()