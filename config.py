import os
import dotenv

##################
PRODUCTION = False
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

# if PRODUCTION is True:
#     TOKEN = os.environ['TOKEN']
#     CONFESSION = os.environ['CONFESSION']
#     APPLICATION = os.environ['APPLICATION']
# else:
    dotenv.load_dotenv()
    TOKEN = os.environ.get('TOKEN')
    CONFESSION = os.environ.get('CONFESSION')
    APPLICATION = os.environ.get('APPLICATION')
