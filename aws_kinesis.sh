# create a stream
aws kinesis create-stream --stream-name <stream-name> --shard-count <shard-count>

aws kinesis create-stream --stream-name MyDataStream --shard-count 1

# describe a stream

aws kinesis describe-stream --stream-name <stream-name>

aws kinesis describe-stream --stream-name MyDataStream

# produce data to a stream

aws kinesis put-record --stream-name MyDataStream --partition-key part1 --data "Hello" --cli-binary-format raw-in-base64-out

# consume data from a stream

aws kinesis get-shard-iterator --stream-name MyDataStream --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON

aws kinesis get-records --shard-iterator <shard-iterator>

# delete a stream

aws kinesis delete-stream --stream-name MyDataStream


--cli-binary-format raw-in-base64-out: This option is used to specify that the data provided in the 
--data parameter should be treated as binary and will be base64-encoded before sending it to the Kinesis Data Stream.
