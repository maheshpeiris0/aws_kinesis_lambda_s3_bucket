import boto3
import time

def process_records(records):
    for record in records:
        # Process the data in the record
        data = record['Data']
        print("Received data:", data.decode('utf-8'))

def kinesis_consumer(stream_name, shard_iterator_type='TRIM_HORIZON', sleep_time=1):
    client = boto3.client('kinesis')

    # Get the shard ID of the first shard in the stream
    response = client.describe_stream(StreamName=stream_name)
    shard_id = response['StreamDescription']['Shards'][0]['ShardId']

    # Get a shard iterator for the specified shard
    shard_iterator_response = client.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType=shard_iterator_type
    )
    shard_iterator = shard_iterator_response['ShardIterator']

    while True:
        # Get the records from the shard iterator
        get_records_response = client.get_records(ShardIterator=shard_iterator)
        records = get_records_response['Records']
        
        if records:
            process_records(records)

        # If there are no records, wait before making the next request
        time.sleep(sleep_time)

        # Update the shard iterator for the next set of records
        shard_iterator = get_records_response['NextShardIterator']

if __name__ == "__main__":
    stream_name = "test" # Change this to your stream name
    kinesis_consumer(stream_name)
