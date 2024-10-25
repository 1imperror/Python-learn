from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
import asyncio
from crud_functions1 import get_all_products, is_included, add_user

API = ''
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())

router = Router()


button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb = ReplyKeyboardMarkup(
    keyboard=[
        [button1, button2, button4],
        [button3]
    ],
    resize_keyboard=True
)


def inl_key_calories():
    kbi = InlineKeyboardBuilder()
    kbi.row(
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    )
    return kbi.as_markup()


def inl_key_bye():
    kbi_1 = InlineKeyboardBuilder()
    kbi_1.row(
        InlineKeyboardButton(text='Product1', callback_data='product_buying'),
        InlineKeyboardButton(text='Product2', callback_data='product_buying'),
        InlineKeyboardButton(text='Product3', callback_data='product_buying'),
        InlineKeyboardButton(text='Product4', callback_data='product_buying')
    )
    return kbi_1.as_markup()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@router.message(F.text == 'Регистрация')
async def sing_up(message, state: FSMContext):
    await message.answer(f"Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)


@router.message(RegistrationState.username)
async def set_username(message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await state.set_state(RegistrationState.email)


@router.message(RegistrationState.email)
async def set_email(message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await state.set_state(RegistrationState.age)


@router.message(RegistrationState.age)
async def set_age(message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    username = data.get('username')
    email = data.get('email')
    age = data.get('age')
    add_user(username, email, age)
    await state.clear()
    await message.answer("Регистрация прошла успешно!")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.message(Command('start'))
async def start(message):
    await message.answer(f"Приветствую, {message.from_user.first_name}! Я бот помогающий твоему здоровью. "
                         f"Нажмите клавишу 'Рассчитать' и мы начнем. Если вы хотите приобрести витамины, "
                         f"то нажмите клавишу 'Купить'", reply_markup=kb)


@router.message(F.text == 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inl_key_calories())


@router.message(F.text == 'Купить')
async def get_buying_list(message):
    get = get_all_products()
    await message.answer_photo(photo=FSInputFile('files/1.png'), caption=f'Название: {get[0][1]} | '
                                                                         f'Описание: {get[0][2]} | Цена: {get[0][3]}')
    await message.answer_photo(photo=FSInputFile('files/2.jpeg'), caption=f'Название: {get[1][1]} |'
                                                                          f' Описание: {get[1][2]} | Цена: {get[1][3]}')
    await message.answer_photo(photo=FSInputFile('files/3.jpg'), caption=f'Название: {get[2][1]} |'
                                                                         f' Описание: {get[2][2]} | Цена: {get[2][3]}')
    await message.answer_photo(photo=FSInputFile('files/4.jpg'), caption=f'Название: {get[3][1]} |'
                                                                         f' Описание: {get[3][2]} | Цена: {get[3][3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inl_key_bye())


@router.callback_query(F.data == 'formulas')
async def get_formulas(query: CallbackQuery):
    await query.message.edit_text('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await query.answer()


@router.callback_query(F.data == 'product_buying')
async def send_confirm_message(query: CallbackQuery):
    await query.message.edit_text('Вы успешно приобрели продукт!')
    await query.answer()


@router.callback_query(F.data == 'calories')
async def set_age(query: CallbackQuery, state: FSMContext):
    await query.message.answer('Введите свой возраст:')
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


@router.message()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    dp = Dispatcher()
    asyncio.run(main())
