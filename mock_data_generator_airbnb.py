import json
import boto3
import random
import string

def data_generator():
    
    message = {
        "bookingId":str(random.randint(100000, 999999)),
        "userId":''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)),
        "propertyId":''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)),
        "location":random.choice(["Tampa, Florida","Hyd, Ind","BLR,Ind"]),
        "startDate":random.choice(["2024-03-12","2024-03-13","2024-03-14"]),
        "endDate":random.choice(["2024-03-13","2024-03-14","2024-03-15"]),
        "price":'$ ' + str(random.randint(100,999))
    }
    
    return message


def lambda_handler(event, context):
    
    sqs = boto3.client('sqs')
    for i in range(5):
        sqs.send_message(QueueUrl='https://sqs.ap-south-1.amazonaws.com/062473133899/airbnb-booking-ritayan', MessageBody=json.dumps(data_generator()))
