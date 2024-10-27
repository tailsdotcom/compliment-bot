BLOCK_COMPLIMENT_BASE = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "",
    },
}

BLOCK_DIVIDER = {"type": "divider"}

import copy


def get_compliment_block(msg):
    result = copy.deepcopy(BLOCK_COMPLIMENT_BASE)
    result["text"]["text"] = msg

    return result
