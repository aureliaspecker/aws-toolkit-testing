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
    polls_data = json.load(json_file)["includes"]["polls"]

connection = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, db=DBNAME)
cursor = connection.cursor()

sql = "REPLACE INTO polls (poll_id, option_1, votes_1,  option_2, votes_2, option_3, votes_3, option_4, votes_4,  duration_minutes, end_datetime, voting_status) VALUES \n"

for poll in polls_data:
    if poll["voting_status"] == "open":
        poll_id = connection.escape(poll["id"])
        for option in poll["options"]:
            if option["position"] == 1:
                option_1 = connection.escape(option["label"])
                votes_1 = 'NULL'
            elif option["position"] == 2:
                option_2 = connection.escape(option["label"])
                votes_2 = 'NULL'
            elif option["position"] == 3:
                option_3 = connection.escape(option["label"])
                votes_3 = 'NULL'
            elif option["position"] == 4:
                option_4 = connection.escape(option["label"])
                votes_4 = 'NULL'
            else: 
                print("Something is wrong")
    elif poll["voting_status"] == "closed":
        poll_id = connection.escape(poll["id"])
        for option in poll["options"]:
            if option["position"] == 1:
                option_1 = connection.escape(option["label"])
                votes_1 = connection.escape(option["votes"])
            elif option["position"] == 2:
                option_2 = connection.escape(option["label"])
                votes_2 = connection.escape(option["votes"])
            elif option["position"] == 3:
                option_3 = connection.escape(option["label"])
                votes_3 = connection.escape(option["votes"])
            elif option["position"] == 4:
                option_4 = connection.escape(option["label"])
                votes_4 = connection.escape(option["votes"])
            else: 
                print("Something is wrong")
    else: 
        print("Could not get poll status")
    try:
        duration_minutes = connection.escape(poll["duration_minutes"])
    except:
        duration_minutes = 'NULL'
    try: 
        end_datetime = connection.escape(poll["end_datetime"])
    except: 
        end_datetime = 'NULL'
    try:
        voting_status = connection.escape(poll["voting_status"])
    except:
        voting_status = 'NULL'
    
    if option_3 in globals():
        pass
    else: 
        option_3 = 'NULL'
        votes_3 = 'NULL'

    if option_4 in globals():
        pass
    else: 
        option_4 = 'NULL'
        votes_4 = 'NULL'

    sql += f"({poll_id}, {option_1}, {votes_1}, {option_2}, {votes_2}, {option_3}, {votes_3}, {option_4}, {votes_4}, {duration_minutes}, {end_datetime}, {voting_status}), \n"

sql = sql[:-3] + ";"
print(sql.count)
print(sql)
     
cursor.execute(sql)
connection.commit()

connection.close()