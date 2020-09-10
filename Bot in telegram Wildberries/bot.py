import asyncio
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from wildberries import Wildberries
from config import TOKEN

wb = Wildberries()
url = wb.get_url(1)
lastkey = wb.get_lastkey(1)
new = wb.new_clothes(url,lastkey)
print(lastkey)
