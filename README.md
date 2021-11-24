[![Digital land smoke test](https://github.com/digital-land/smoke-test/actions/workflows/smoke-test.yml/badge.svg)](https://github.com/digital-land/smoke-test/actions/)


# smoke-test

Smoke tests for [www.digital-land.info](www.digital-land.info])

The tests in [tests/test_site.py](tests/test_site.py) are run as a github
action every 15 minutes. 

Test failures are relayed to the dl-developers Slack channel using a
webhook url for the Slack smoke-test-app.

The reporting of test failures is handled by [report/slack_error.py](report/slack_error.py)
