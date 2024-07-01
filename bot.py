from aiogram import Bot , Dispatcher , executor , types
import random
from config import token
numbers = random.randint(1, 3)
bot = Bot(token=token)
db = Dispatcher(bot)

@db.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("Привет!\n Я бот давай поиграем в игру где я загадаю число ты должен угадать число")

@db.message_handler(commands="/play")
async def play(message:types.Message):
    await message.answer("Угадайте число от 1 до 3")

@db.message_handler()
async def guess_num(message: types.Message):
    guess = int(message.text)
    if guess == numbers:
        await message.answer("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer("https://media.makeameme.org/created/sorry-you-lose.jpg")

executor.start_polling(db, skip_updates=True)