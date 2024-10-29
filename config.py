from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26614080"
# -------------------------------------------------------------
API_HASH = "7d2c9a5628814e1430b30a1f0dc0165b"
# --------------------------------------------------------------
BOT_TOKEN = getenv("7893591023:AAHwF4wSKnrSln7lkhJs3e947Ro6xS52arc", None)
MONGO_URL = getenv("mongodb+srv://lejato8322:lzGK1qFJs3t5VTPQ@cluster0.1ccf7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)
OWNER_ID = int(getenv("OWNER_ID", "5606990991"))
SUPPORT_GRP = "Team_Pbail"
UPDATE_CHNL = "Ps_Support_Group"
OWNER_USERNAME = "Pbail"
