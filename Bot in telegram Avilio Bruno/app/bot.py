import asyncio
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from stopgame import StopGame
from config import TOKEN

bot = Bot(token = TOKEN) # Инициализируем объекты бота 
dp = Dispatcher(bot) # Инициализируем диспетчера

# Инициализируем парсер
sg = StopGame()
# проверяем наличие новых игр и делаем рассылки
async def scheduled(wait_for):
	while True:
		await asyncio.sleep(wait_for)

		# проверяем наличие новых игр
		new_games = sg.new_games()

		if(new_games):
			# если игры есть, переворачиваем список и итерируем
			new_games.reverse()
			for ng in new_games:
				# парсим инфу о новой игре
				nfo = sg.game_info(ng)

				# отправляем всем новость
				await bot.send_photo(
							'768700960',
							nfo['image'],
							caption = nfo['title'] + "\n" + "Оценка: " + nfo['score'] + "\n" + nfo['excerpt'] + "\n\n" + nfo['link'],
							disable_notification = True
						)

#@dp.message_handler(commands = ['start'])
#async def process_start_command(message: types.Message):
#    await message.reply("Привет.\nЯ живой. Усе работает. Напиши /help.")
#
#@dp.message_handler(commands=['help'])
#async def process_help_command(message: types.Message):
#    msg = text(bold('Я могу ответить на следующие команды:'),
#               '/voice', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
#    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


#VOICE = open('voise/apihost.ru_voice.mp3', 'rb')

#@dp.message_handler(commands=['voice'])
#async def process_voice_command(message: types.Message):
#    await bot.send_voice(message.from_user.id, VOICE, reply_to_message_id=message.message_id)

#IMG = open('img/img.jpg', 'rb')

#@dp.message_handler(commands=['photo'])
#async def process_photo_command(message: types.Message):
#    caption = 'Какие глазки! :eyes:'
#    await bot.send_photo(message.from_user.id, IMG,
#                         caption=emojize(caption),
#                         reply_to_message_id=message.message_id)

#@dp.message_handler()
#async def echo_message(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)

    
if __name__ == '__main__':
	dp.loop.create_task(scheduled(10)) # пока что оставим 10 секунд (в качестве теста)
	executor.start_polling(dp, skip_updates=True)