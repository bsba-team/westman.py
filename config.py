import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')
CONFESSION = os.environ.get('CONFESSION')

PERSON = [
    "Westman",
    "Southman",
    "Northman",
    "Eastman"
]

DIALOG = [
    "wanted to say that",
    "told that",
    "said that",
    "disclosed",
    "announced"
]


CONTENT = [
    "wanted to share that",
    "wanted to show that"
]

OFFENSIVE = [
    "suka",
    "blyat"
]
