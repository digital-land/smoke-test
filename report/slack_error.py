import sys
import os
import click
import requests


@click.command()
@click.option(
    "--slackurl", help="The webhook url for slack app you're posting to", required=True
)
@click.option(
    "--github_run_number", help="Url for failed test run", required=True
)
def post_error_to_slack(slackurl, github_run_number):
    github_actions_link = f"https://github.com/digital-land/smoke-test/runs/{github_run_number}?check_suite_focus=true"
    requests.post(
        slackurl,
        json={
            "text": f"Smoke tests failed - details here {github_actions_link}"
        },
    )


if __name__ == "__main__":
    post_error_to_slack()
    sys.exit(-1)
