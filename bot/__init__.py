import os
import sys
import time
import logging

from dotenv import load_dotenv

import telegram.ext as tg


# Setup logger
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)

START_TIME = time.time()

# Check python version
if sys.version_info[0] < 3 or sys.version_info[1] < 9:
    LOGGER.error(
        "Hello dear, you mush have python version of at least 3.9! So go install the new version."
    )

load_dotenv()

TOKEN = os.environ.get('TOKEN', None)
DB_URI = os.environ.get('DB_URI', None)
API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)

DOWNLOAD_LOCATION = "./Downloads"
DOWNLOAD_START = "Give Me Some Time..."
CUSTOM_CAPTION_UL_FILE = " "
SAVED_RECVD_DOC_FILE = "File Downloaded Successfully 😎"
UPLOAD_START = "Starting to upload..."
AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me > ©  @RetroginiBots **"
bot = Client("Rename-Bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


bot.run()
