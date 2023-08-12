import json
import boto3
import time
from data_generator import make_employee

stream_name = 'test' # Kinesis Data Stream Name


def main():
    kinesis = boto3.client('kinesis')

    while True:
        # Generate fake employee data
        employee = make_employee()
        print(f'Generated {employee}')

        try:
            # execute single PutRecord request
            response = kinesis.put_record(StreamName=stream_name,
                                          Data=json.dumps(employee).encode('utf-8'),
                                          PartitionKey=employee['employee_id'])
            print({  # log successful response
                'message': 'Successfully produced record',
                'response': response,
                'record': employee
            })
        except Exception as e:
            print({  # log exception
                'message': 'Failed to produce record',
                'exception': e,
                'record': employee
            })
        time.sleep(0.3)



if __name__ == '__main__':
    main()
