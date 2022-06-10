



from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSID = int(getenv("ASSID"))
ASSNAME = getenv("ASSNAME")
ASSUSERNAME = getenv("ASSUSERNAME")
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/kaal0408/Music")
USERS = getenv("2068551800")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
UPDATE = getenv("UPDATE")
SUPPORT = getenv("SUPPORT")
START_IMG = getenv("START_IMG")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f6d20eb3b3a7c810c09a0.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2068551800").split()))
ASSISTANT_NAME = getenv("ASSNAME")
COMMAND_PREFIXES = ("/ ! .").split()
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e4de79101db015f156f39.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/773b9323c15fa1b48a576.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a8fdd2fc7e619111d7605.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/3f60b051a756875ff73fb.jpg")
