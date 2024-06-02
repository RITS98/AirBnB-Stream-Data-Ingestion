# AirBnB-Stream-Data-Ingestion
Build a simulated data pipeline for Airbnb booking data that integrates various AWS services, demonstrating real-time data processing, filtering, and storage.

## Technologies Used
  1. AWS SQS
  2. AWS Lambda
  3. AWS S3
  4. AWS Event Bridge
  5. Python
  6. Git

## Steps
  1. Create a SQS service
     ![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/2057ad03-47a1-4264-995b-4a3449694fe3)

     Dead Letter Queue Configuration
     ![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/a64089da-6c26-4a6c-8107-0030f6526228)

  2. Create a mock data generator in python and place it in lambda
     ![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/a3b5f9a9-252d-4b4c-bde0-1763d9a3192b)

  3. Give relevant access to the Lambda
     ![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/7c36ae37-4b8c-4894-bdcd-4bdd75b59096)

  4. Go to AWS Event Bridge and create a event pipe
     ![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/94bcadbf-e6cb-42c6-9ca2-1bd9a08ffdb4)

     a. Add the SQS as source
     b. Remove the filtering step
     c. Add the enrichment lambda code
     d. Add the data loading to S3 Lambda code

     ![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/7a8dcb4a-a592-41b6-9bbf-e6ad76f9005d)

## Output
### Data Load to S3 Lambda Output Logs
![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/820fc2eb-7f0d-4b97-b3fc-27c9cce8f296)

### Output CSV File
![image](https://github.com/RITS98/AirBnB-Stream-Data-Ingestion/assets/51791113/f4ebed22-3572-4d04-a681-1be3c2bd83fc)


