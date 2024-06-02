import json
import boto3
import pandas as pd
from datetime import date
import time
import io
import os

def lambda_handler(event, context):
    print('Event : ', event)
    print('Context : ', context)
    message=event[0]['message']
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    today_date = str(date.today())
    print('Message : ', message)
    
    if message == {}:
        return {}
    else:
        try:
            print("Inside Try ")
            obj = s3_client.get_object(Bucket='airbnb-data-store-ritayan', Key = f'{today_date}/Airbnb_{today_date}.csv')
            obj = obj['Body'].read()
            obj=str(obj, 'utf-8')
            data=io.StringIO(obj)
            print("Data -> ", data)
            df=pd.read_csv(data, index_col='bookingId')
            df.loc[message['bookingId']] = [message['userId'], message['propertyId'], message['location'], message['startDate'], message['endDate'], message['price']]
            print(df)
            df.to_csv('/tmp/test.csv', encoding='utf-8')
            s3_resource.Bucket('airbnb-data-store-ritayan').upload_file('/tmp/test.csv', f'{today_date}/Airbnb_{today_date}.csv')
            print('Data Uploaded Try')
        except Exception as e:
            
            print('Exception :-------- ', str(e))
            df = pd.DataFrame(columns = ['bookingId','userId','propertyId','location','startDate','endDate','price'])
            
            df = df.set_index(list(df.columns)[0])
            df.loc[message['bookingId']] = [message['userId'],message['propertyId'],
                                    message['location'],message['startDate'],message['endDate'],
                                    message['price']]  
            print(df)
            df.to_csv('/tmp/test.csv',encoding='utf-8')
            s3_resource.Bucket('airbnb-data-store-ritayan').upload_file('/tmp/test.csv',f'{today_date}/Airbnb_{today_date}.csv')
            print('Data Uploaded Exception')
