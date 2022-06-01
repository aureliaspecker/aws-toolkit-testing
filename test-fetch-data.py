import sys
import json
from fetch_tweets import Recent_Search

# Change query, start and end times for request. 
# Start and end times must be within the last 7 days.
query = "context:131.1220701888179359745 lang:en"
max_results = 100
start_time = "2022-05-31T09:50:00Z" 
end_time = "2022-05-31T10:00:00Z"
tag = "covid"

# Uploads response payload to S3 bucket
def put_tweets(query, max_results, start_time, end_time):

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
        with open(f"{tag}-{request_count}.json", "w+") as f:
            f.write(json.dumps(data) + "\n") 
        if "next_token" not in meta:
            break
        next_token = meta["next_token"]
        query_parameters.update(next_token = next_token)
    
    return(request_count)

if __name__ == "__main__":
    request_count = put_tweets(query, max_results, start_time, end_time)
    print(f"Number of requests: {request_count}")
             