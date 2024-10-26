import random

from service.messages import BLOCK_DIVIDER, COMPLIMENT_MSG, CONFIRMATION_MSG, COMPLIMENT_HEADER, get_compliment_block, ACCESSORY_COMPLIMENT, ACCESSORY_INSULT

COMPLIMENT_CHANCE: float = 1

class ComplimentService:
    def __init__(self):
        self.mode = "insult" if random.random() > COMPLIMENT_CHANCE else "compliment"

    def reroll_compliment(self):
        self.mode = "insult" if random.random() > COMPLIMENT_CHANCE else "compliment"

    @property
    def insult(self):
        return self.mode == "insult"

    def _get_msg_context(self, recipients, sender=None, message=None):
        names = [user["real_name"] for user in recipients]
        if len(recipients) > 1:
            recipient_names = '{}, and {}'.format(', '.join(names[:-1]), names[-1])
        else:
            recipient_names = names[0]
        
        context = {
            "recipient_names": recipient_names,
            "have_has": "has" if len(recipients) > 1 else "have",
        }

        if sender:
            context.update(
                {"sender_name": sender["real_name"]}
            )
        
        if message:
            context.update(
                {"message": message}
            )
        
        return context


    def get_confirmation_msg(self, sender, recipients) -> str:
        msg = random.choice(CONFIRMATION_MSG[self.mode])

        context = self._get_msg_context(recipients, sender)

        return msg.format(
            **context
        )

    def get_compliment(self, sender, recipients, message: str) -> str:
        context = self._get_msg_context(recipients, sender, message)

        default_msg = random.choice(COMPLIMENT_MSG[self.mode]).format(**context)

        block_header = get_compliment_block(random.choice(COMPLIMENT_HEADER[self.mode]))

        body_block = get_compliment_block(default_msg)
        if self.insult: 
            body_block.update(
                ACCESSORY_INSULT #  else ACCESSORY_COMPLIMENT
            )

        blocks = [
            block_header,
            BLOCK_DIVIDER.copy(),
            body_block
        ]

        if self.insult:
            blocks.append(BLOCK_DIVIDER.copy())
            
            blocks.append(get_compliment_block("This is what they _really_ said..."))

            blocks.append(get_compliment_block(f">{message}"))

        return default_msg, blocks
