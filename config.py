from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/0eab6ba8b0302de6507fc.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PanjabxMusic")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ogsupportchatt")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6061809727").split()))


FAILED = "https://graph.org/file/eb37c0273e513e5a88ba4.jpg"
