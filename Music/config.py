##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "6435225"))
API_HASH = getenv('API_HASH', '4e984ea35f854762dcde906dce426c2d')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ ! .').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://TGN:TGN@cluster0.c4yk3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1669178360').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001447540388'))
ASS_ID = int(getenv("ASS_ID", '2074055358'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1669178360').split()))
