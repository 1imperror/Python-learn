from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio

API = '7826127560:AAGJ7ca22b_fSwlygGVFufumYXo3hbm3p4k'
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())

router = Router()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.message(Command('start'))
async def start(message):
    await message.answer(f"Приветствую, {message.from_user.first_name}! Я бот помогающий твоему здоровью. "
                         f"Введите слово Calories и я посчитаю вашу норму калорий.")


@router.message(F.text == 'Calories')
async def set_age(message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@router.message(UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@router.message(UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@router.message(UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    form = (10 * int(data['weight'])) + (6.25 * int(data['growth']) - (5 * int(data['age'])))
    await message.answer(f'Ваша норма калорий {form}')
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    dp = Dispatcher()
    dp.include_router(router)
    asyncio.run(main())
