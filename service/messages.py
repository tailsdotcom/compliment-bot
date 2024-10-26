CONFIRMATION_MSG = {
    "insult": [
        "Ooops! The bot broke and {recipient_names} {have_has} been insulted instead",
        "{sender_name}? You are on the naughty list! We've sent an insult to {recipient_names} instead",
        ":ragebagel: gains not detected :ragebagel: compliment rejected :ragebagel:",
        "What you said was nice, but... We've gone with a different approach."
    ],
    "compliment": [
        "Compliment sent to {recipient_names}!",
    ]
}

COMPLIMENT_MSG = {
    "insult": [
        "Someone wanted to send you a compliment but we lost it. Don't worry, it wasn't very good anyway.",
        "{recipient_names}? Someone would like you to stop it now pls",
        "You got nice elbows. I don't know what that means either.",
        "Your mother was a hamster, and your father smells of elderberries.",
        ":ragebagel: gains not detected :ragebagel: compliment rejected :ragebagel:",
        "We sent you a compliment, but you need to understand it's opposite day.",
        "You've been given a nice message. Enjoy it. It's the last one.", 
        "Here's an insult from Leanne Earthey, PD from Shop Squad: ur ginger lmao",
        "Gonna reject your PR. If you're not a dev, I'm going to teach you how to make a PR, then reject it."
        "You probably think Die Hard is a Christmas movie",
        "You eat Bounty bars."
        ":alberto-maate: you think Domino's is authentic Italian pizza :alberto-maate:",
        
        
    ],
    "compliment": [
        "{message}",
    ]
}

COMPLIMENT_HEADER = {
    "insult": [
        "Someone sent you a compliment!",
    ],
    "compliment": [
        "Someone sent you a compliment!",
    ]
}

ACCESSORY_COMPLIMENT = {
    "accessory": {
        "type": "image",
        "image_url": "https://compliment-bot.s3.eu-west-1.amazonaws.com/assets/happymensch.png",
        "alt_text": "You've been complimented!"
    }
}

ACCESSORY_INSULT = {
    "accessory": {
        "type": "image",
        "image_url": "https://compliment-bot.s3.eu-west-1.amazonaws.com/assets/hypermensch.png",
        "alt_text": "You've been insulted!"
    }
}

BLOCK_COMPLIMENT_BASE = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "",
    }
}

BLOCK_DIVIDER = {
    "type": "divider"
}

import copy

def get_compliment_block(msg):
    result = copy.deepcopy(BLOCK_COMPLIMENT_BASE)
    result["text"]["text"] = msg

    return result