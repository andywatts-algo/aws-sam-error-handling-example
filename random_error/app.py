import json, random

class TaskFailedException(Exception):
    pass

def lambda_handler(event, context):
    if random.random() < 0.5:
        raise TaskFailedException(json.dumps({
            "error": "TaskFailedException",
            "cause": "Task failed intentionally"
        }))
    return {"statusCode": 200, "body": json.dumps({"message": "Success!"})}
