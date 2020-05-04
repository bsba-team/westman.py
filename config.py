import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')
CONFESSION = os.environ.get('CONFESSION')
APPLICATION = os.environ.get('APPLICATION')

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
