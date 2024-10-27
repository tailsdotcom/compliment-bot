import logging
import re

import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackService:
    def __init__(self, slack_token):
        self.client = WebClient(token=slack_token)

    def process_slack_message(self, message: str):
        escaped_elements = re.findall(r"<.*?>", message)
        users = [l.split("|")[0][2:] for l in escaped_elements if "|" in l and "@" in l]

        message_regex = re.compile(r"(<@.*?>\s?)+(.*)")
        message_elements = message_regex.match(message)

        return users, message_elements.group(2)

    def get_user_info(self, user_id: str):
        try:
            response = self.client.users_info(user=user_id)

            if response["ok"]:
                return response["user"]
            else:
                logging.info(response["error"])
        except SlackApiError as e:
            logging.error(f"Failed to get details for user {user_id}", e)

        return {}

    def send_ephemeral_response(self, msg, response_url):
        try:
            payload = {"text": msg, "response_type": "ephemeral"}

            requests.post(response_url, json=payload)
        except Exception as e:
            logging.error(e)

    def send_private_message(self, channel_id, msg, blocks=None) -> None:
        try:
            response = self.client.chat_postMessage(
                channel=channel_id, text=msg, blocks=blocks
            )
        except SlackApiError as e:
            logging.error(f"Failed to send message to channel {channel_id}", e)
