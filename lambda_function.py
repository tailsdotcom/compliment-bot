import base64
import logging
import os

from urllib.parse import parse_qs

from service.compliment_bot import ComplimentBot
from service.slack_service import SlackService

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO, force=True)


def respond(err, res=None):
    rsp = {
        "statusCode": "400" if err else "200",
        "headers": {
            "Content-Type": "application/json",
        },
    }
    if res:
        rsp.update({"body": err.message if err else json.dumps(res).encode("utf8")})
    return rsp


def lambda_handler(event, context):
    slack_token = os.environ["SLACK_TOKEN"]

    params = parse_qs(base64.b64decode(event["body"]))
    user = params[b"user_id"][0].decode("utf-8")
    response_url = params[b"response_url"][0].decode("utf-8")
    if b"text" in params:
        command_text = params[b"text"][0].decode("utf-8")
    else:
        command_text = ""

    slack_service = SlackService(slack_token)
    compliment_bot = ComplimentBot(slack_service)

    compliment_bot.compliment(user, command_text, response_url)

    return respond(None)
