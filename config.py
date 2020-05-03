import os
import dotenv

##################
PRODUCTION = True
##################

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

if PRODUCTION is True:
    TOKEN = os.environ.get('TOKEN')
    CONFESSION = os.environ.get('CONFESSION')
    APPLICATION = os.environ.get('APPLICATION')

else:
    dotenv.load_dotenv()
    TOKEN = os.environ.get('TOKEN')
    CONFESSION = os.environ.get('CONFESSION')
    APPLICATION = os.environ.get('APPLICATION')
