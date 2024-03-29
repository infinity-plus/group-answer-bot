"""The main package of AddMe Bot."""

import logging
from os import environ

from telegram.ext import Dispatcher, Updater
from ptbcontrib.postgres_persistence import PostgresPersistence

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

DB_URI = environ.get("DATABASE_URL", "")
if DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)
TOKEN = environ.get("TOKEN", "")
WEBHOOK = bool(environ.get("WEBHOOK", False))
URL = environ.get("URL", "")  # Does not contain token
PORT = int(environ.get("PORT", 5000))


UPDATER: Updater = Updater(
    token=TOKEN,
    arbitrary_callback_data=True,
    persistence=PostgresPersistence(url=DB_URI),
)
DISPATCHER: Dispatcher = UPDATER.dispatcher
