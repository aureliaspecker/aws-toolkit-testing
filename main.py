# To Do's: 
# [✔] Create class to authenticate to the Twitter API.
# [✔] Create class to connect to Recent search API with pagination.
# [✔] PUT new response payloads in S3 bucket (object name to reflect request count + current date time)
# [✔] New data in S3 bucket triggers Lambda function to process and store the data in a MySQL DB (RDS).
# [ ] Develop more complext schema and multiple tables to store all fields and expansions.
# [ ] Figure out infrastructure as code layer.

# ============================================================================
# To set your environment variables in the command line run the following line:
# export 'TWITTER_BEARER_TOKEN'='<your_bearer_token>'

# AWS credentials are expected to be found in ~.aws/credentials and ~.aws/config

import sys
import boto3
from botocore.exceptions import ClientError
import json
import datetime as dt
from fetch_tweets import Recent_Search

# Change query, start and end times for request. 
# Start and end times must be within the last 7 days.
query = "context:86.1367860707362926592 lang:en"
max_results = 100
start_time = "2022-04-24T18:30:00Z" 
end_time = "2022-04-24T19:00:00Z"

s3 = boto3.resource('s3')

# Uploads response payload to S3 bucket
def put_tweets(query, max_results, start_time, end_time, s3):

    request_count = 0

    fetch_data = Recent_Search()

    query_parameters = {
        "query": query,
        "max_results": max_results, 
        "start_time": start_time,
        "end_time": end_time
        }

    while True: 
        response = fetch_data(query_parameters)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        request_count += 1
        response_payload = response.json()
        meta = response_payload["meta"]
        # data = response_payload["data"]
        data = response_payload
        if meta["result_count"] == 0:
            sys.exit("No replies to analyze")
        now = dt.datetime.utcnow()
        dt_string = now.strftime("%Y%m%d%H%M%S")
        # Replace "search-tweets" with bucket name
        s3object = s3.Object('search-tweets', f'payload-{request_count}-{dt_string}.json')
        s3object.put(
            Body=(bytes(json.dumps(data).encode('UTF-8')))
            )
        print(data)
        if "next_token" not in meta:
            break
        next_token = meta["next_token"]
        query_parameters.update(next_token = next_token)
    
    return(request_count)

if __name__ == "__main__":
    request_count = put_tweets(query, max_results, start_time, end_time, s3)
    print(f"Number of requests: {request_count}")
