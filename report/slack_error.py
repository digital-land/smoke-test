import requests
import os

SLACK_URL = os.environ.get("SLACK_WEBHOOK_URL")
if SLACK_URL is not None:
    requests.post(SLACK_URL, json={"text":"this is a test"})