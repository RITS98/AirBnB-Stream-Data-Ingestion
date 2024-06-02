import json

def lambda_handler(event, context):
    try:
        print('Event : ', event)
        print('Context: ', context)
        message = json.loads(event[0]['body'])
        if message['startDate'] == message['endDate'] :
            message = {}
        else:
            return {
             'message':message
        }
            
            
    except Exception as e:
        return {
            'Error message':str(e)
        }
