import logging

from service.compliment_service import ComplimentService


class ComplimentBot:
    def __init__(self, slack_service):
        self.slack_service = slack_service

    def compliment(self, user_id: str, text: str, response_url: str) -> bool:
        users, message = self.slack_service.process_slack_message(text)

        sender = self.slack_service.get_user_info(user_id)
        recipients = [self.slack_service.get_user_info(id) for id in users]

        logging.info(f"user {sender['name']} | message {text}")

        compliment_service = ComplimentService()

        self.slack_service.send_ephemeral_response(
            compliment_service.get_confirmation_msg(sender, recipients), response_url
        )

        compliment_message, compliment_blocks = compliment_service.get_compliment(
            sender, recipients, message
        )
        for recipient in recipients:
            self.slack_service.send_private_message(
                recipient["id"], compliment_message, compliment_blocks
            )
