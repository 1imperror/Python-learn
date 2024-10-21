from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
import asyncio

API = ''
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command('start'))
async def start(message):
    await message.answer(f"Приветствую, {message.from_user.first_name}!")
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
