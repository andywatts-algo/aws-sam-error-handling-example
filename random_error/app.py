import json, random

class TaskFailedException(Exception):
    pass

def lambda_handler(event, context):
    print(event)
    if random.random() < 0.5:
        raise TaskFailedException(json.dumps({
            "error": "TaskFailedException",
            "cause": "Task failed intentionally"
        }))
    return {"message": "random_error_output", "input": event}
