import base64
import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print('Received Kinesis records:', json.dumps(event, indent=2))
    
    s3_bucket = 'S3 Bucket Name' # Adjust the S3 bucket as needed
    s3_key = 'kinesis-records/all_records.txt'  # Adjust the S3 key as needed

    combined_payloads = ""

    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print('Kinesis record payload:', payload)
        
        combined_payloads += payload + "\n"
        
    # Retrieve the existing content of the file, if it exists
    try:
        existing_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
        existing_payloads = existing_object['Body'].read().decode('utf-8')
        combined_payloads = existing_payloads + combined_payloads
    except s3_client.exceptions.NoSuchKey:
        pass  # If the file doesn't exist yet, we'll create it
    
    # Upload the combined payloads to the same file in S3
    s3_client.put_object(Bucket=s3_bucket, Key=s3_key, Body=combined_payloads)
    print(f"Uploaded to S3: s3://{s3_bucket}/{s3_key}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Records processed and appended to S3.'),
    }
