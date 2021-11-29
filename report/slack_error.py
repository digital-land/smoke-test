import click
import requests


@click.command()
@click.option('--slackurl', help="The webhook url for slack app you're posting to", required=True)
def post_error_to_slack(slackurl):
    requests.post(slackurl, json={"text":"Smoke tests failed - details here https://github.com/digital-land/smoke-test/actions"})


if __name__ == '__main__':
    post_error_to_slack()
