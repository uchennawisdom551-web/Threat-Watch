import boto3
import gzip
import json
from io import BytesIO
import pandas as pd

s3 = boto3.client(
    "s3", endpoint_url="http://172.16.32.163:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)
BUCKET = "cloud-info"
PREFIX = "AWSLogs/000000000000/CloudTrail/"


response = s3.list_objects_v2(
    Bucket=BUCKET,
    Prefix=PREFIX
)

events = []
for obj in response.get("Contents", []):
    key = obj["Key"]

    if not key.endswith(".json.gz"):
        continue
    print(f"[+]  Fetching: {key}")

    result = s3.get_object(
        Bucket=BUCKET,
        Key=key
 )
    compressed = result["Body"].read()

    with gzip.GzipFile(fileobj=BytesIO(compressed)) as gz:
        data = json.loads(gz.read().decode("utf-8"))
        events.extend(data.get("Records", []))
print(f"\n[+] CloudTrail events found: {len(events)}")

processed = []
for event in events:

   processed_events = {"time" : event.get("eventTime"), 
                     "user"   : event.get("userIdentity",{}).get("arn"),
                     "service": event.get("eventSource"),
                     "action" : event.get("eventName"),
                     "region" : event.get( "awsRegion"),
                     "ip"     : event.get("sourceIPAddress"),
                    "readonly": event.get( "readOnly")
}
  
   
   processed.append(processed_events)

df = pd.DataFrame(processed)
df["time"] = pd.to_datetime(df["time"], utc=True)
print(df["time"].min())
print(df["time"].max())
print(df["time"].dtype)
#print(df["time"].head())
print(df["time"].isnull().sum())  


hourly_events = df.groupby(df["time"].dt.floor("h")).size()
print(hourly_events)
print('Events Counted:', len(events))



   

