import logging
import json

def main(event: str):
    try:
        data = json.loads(event)
        logging.info(f"Event received: {data}")
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse event: {e}")
    except Exception as ex:
        logging.error(f"Unhandled error: {ex}")
