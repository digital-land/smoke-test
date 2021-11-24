import requests
import os


SLACK_URL = os.environ.get("SLACK_SMOKE_TEST_WEB_HOOK_URL")
if SLACK_URL is not None:
    requests.post(SLACK_URL, json={"text":"this *just* a test from smoke test trial"})