import json
from datetime import datetime, timezone, timedelta
from requests import request
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened
from twarc_csv import CSVConverter

import logging
import boto3
from botocore.exceptions import ClientError

import os

from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

BEARER_TOKEN = os.getenv("bearer")

s3 = boto3.resource('s3')

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

t = Twarc2(bearer_token=BEARER_TOKEN)

# Start and end times must be in UTC
start_time = datetime.now(timezone.utc) + timedelta(minutes=-2)
# end_time cannot be immediately now, has to be at least 30 seconds ago.
end_time = datetime.now(timezone.utc) + timedelta(minutes=-1)

query = "context:131.1220701888179359745"
tag = "covid"

search_results = t.search_all(query=query, start_time=start_time, end_time=end_time, max_results=100)

request_count = 0

for page in search_results:
    request_count += 1
    result = ensure_flattened(page)
    with open(f"{tag}-{request_count}.jsonl", "w+") as f:
        f.write(json.dumps(result) + "\n")
        print("Wrote a page of results...")
        print("Converting to CSV")
        with open(f"{tag}-{request_count}.jsonl", "r") as infile: 
            with open (f"{tag}-{request_count}.csv", "w") as outfile:
                converter = CSVConverter(infile, outfile)
                converter.process()
                print("Uploading to S3")
                upload_file(f"{tag}-{request_count}.csv", "tweets-flattened")
             
print("Finished.")