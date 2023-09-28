import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://telegra.ph/welcome-pic-07-28 https://telegra.ph/Bean-08-03 https://telegra.ph/cinema-posters-08-05 https://telegra.ph/mala-posters-08-05')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '684256582').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001671146330').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', -1001612868273)
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '👋 𝙷𝙴𝙻𝙾 {user}\n\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {bot},\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽...')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '**𝑯𝒆𝒍𝒍𝒐...\n\n\n𝘊𝘭𝘪𝘤𝘬 𝘰𝘯 🤖 𝗝𝗼𝗶𝗻 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹\n𝘈𝘧𝘵𝘦𝘳 𝘑𝘰𝘪𝘯𝘪𝘯𝘨 𝘵𝘩𝘢𝘵 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 \n𝘊𝘭𝘪𝘤𝘬 🔄 𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻\n\nതാഴെ കാണുന്ന 🤖𝗝𝗼𝗶𝗻 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 എന്ന ബട്ടണിൽ ക്ലിക്ക് ചെയിത് ചാനലിൽ ജോയിൻ ആയതിന് ശേഷം,\n\nതഴെ കാണുന്ന 🔄 𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻 എന്ന ബട്ടണിൽ ക്ലിക്ക് ചെയ്യുക സിനിമ ലഭിക്കുന്നതാണ്...!!**')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hai {user}\nwelcome to {chat}")
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "180"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001877876078))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'cinemahub5k')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "Hey {mention}👋\n\n{file_name}\n\n🍀 size - {file_size}\n\n𝘊𝘩𝘢𝘯𝘯𝘦𝘭 𝘓𝘪𝘯𝘬 @CiNeMaHuB1K\n\n𝘎𝘳𝘰𝘶𝘱 𝘓𝘪𝘯𝘬 @CiNeMaHuB5K")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🏷 Title</b>: <a href={url}>{title}</a>\n‌<b>🎭 Genres</b>: {genres}\n‌<b>📆 Year</b>: <a href={url}/releaseinfo>{year}</a>\n‌<b>🌟 Rating</b>: <a href={url}/ratings>{rating}</a>\n‌<b>☀️ Languages</b> : <code>{languages}</code>\n‌<b>👨‍💼 Dɪʀᴇᴄᴛᴏʀ</b>: {director}\n‌<b>📀 RunTime</b>: {runtime} Minutes\n‌\n‌\n‌<b>🍀Requested by🍀</b> : {message.from_user.mention}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)









