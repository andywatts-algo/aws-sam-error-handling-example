import json, logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(json.dumps(event))
    return {"statusCode": 200, "body": json.dumps({"message": "Event logged"})}
