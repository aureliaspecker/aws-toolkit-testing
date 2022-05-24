from twarc import Twarc2, expansions
import datetime
import json
import os

# To set your environment variables in the command line run the following line:
# export 'TWITTER_BEARER_TOKEN'='<your_bearer_token>'

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Replace your bearer token below
client = Twarc2(bearer_token=BEARER_TOKEN)


def main():
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2022, 5, 22, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2022, 5, 24, 0, 0, 0, 0, datetime.timezone.utc)

    # This is where we specify our query as discussed in module 5
    query = "from:maddie_testing"

    # The search_all method call the full-archive search endpoint to get Tweets based on the query, start and end times
    search_results = client.search_recent(query=query, start_time=start_time, end_time=end_time, max_results=100)

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        for tweet in result:
            # Here we are printing the full Tweet object JSON to the console
            print(json.dumps(tweet))


if __name__ == "__main__":
    main()