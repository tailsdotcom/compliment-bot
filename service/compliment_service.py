from service.messages import BLOCK_DIVIDER, get_compliment_block


class ComplimentService:
    def _get_msg_context(self, recipients, sender=None, message=None):
        names = [user["real_name"] for user in recipients]
        if len(recipients) > 1:
            recipient_names = "{}, and {}".format(", ".join(names[:-1]), names[-1])
        else:
            recipient_names = names[0]

        context = {
            "recipient_names": recipient_names,
            "have_has": "has" if len(recipients) > 1 else "have",
        }

        if sender:
            context.update({"sender_name": sender["real_name"]})

        if message:
            context.update({"message": message})

        return context

    def get_confirmation_msg(self, sender, recipients) -> str:
        msg = "Compliment sent to {recipient_names}!"

        context = self._get_msg_context(recipients, sender)

        return msg.format(**context)

    def get_compliment(self, sender, recipients, message: str) -> str:
        context = self._get_msg_context(recipients, sender, message)

        default_msg = message

        block_header = get_compliment_block("Someone sent you a compliment!")

        body_block = get_compliment_block(default_msg)

        blocks = [block_header, BLOCK_DIVIDER.copy(), body_block]

        return default_msg, blocks
