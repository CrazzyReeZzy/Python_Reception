import asyncio
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from config import TOKEN

bot = Bot(token = TOKEN) # Инициализируем объекты бота 
dp = Dispatcher(bot) # Инициализируем диспетчера

@dp.message_handler(commands = ['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет.\nЯ живой. Усе работает. Напиши /help.")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/voice', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


VOICE = open('voise/apihost.ru_voice.mp3', 'rb')

@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    await bot.send_voice(message.from_user.id, VOICE, reply_to_message_id=message.message_id)

IMG = open('img/img.jpg', 'rb')

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    caption = 'Какие глазки! :eyes:'
    await bot.send_photo(message.from_user.id, IMG,
                         caption=emojize(caption),
                         reply_to_message_id=message.message_id)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

    
if __name__ == '__main__':
    executor.start_polling(dp)