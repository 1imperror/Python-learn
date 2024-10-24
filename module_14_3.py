from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

API = ''
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())

router = Router()


button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb = ReplyKeyboardMarkup(
    keyboard=[
        [button1, button2],
        [button3]
    ],
    resize_keyboard=True
)


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
    kbi = InlineKeyboardBuilder()
    kbi.button(text='Рассчитать норму калорий', callback_data='calories')
    kbi.button(text='Формулы расчёта', callback_data='formulas')
    kbi.adjust(2)
    await message.answer('Выберите опцию:', reply_markup=kbi.as_markup())


@router.message(F.text == 'Купить')
async def get_buying_list(message):
    photo1 = FSInputFile('files/1.png')
    await message.answer_photo(photo1, caption=f'Название: Product{1} | Описание: описание {1} | Цена: {1 * 100}')
    photo2 = FSInputFile('files/2.jpeg')
    await message.answer_photo(photo2, caption=f'Название: Product{2} | Описание: описание {2} | Цена: {2 * 100}')
    photo3 = FSInputFile('files/3.jpg')
    await message.answer_photo(photo3, caption=f'Название: Product{3} | Описание: описание {3} | Цена: {3 * 100}')
    photo4 = FSInputFile('files/4.jpg')
    await message.answer_photo(photo4, caption=f'Название: Product{4} | Описание: описание {4} | Цена: {4 * 100}')
    kbi_1 = InlineKeyboardBuilder()
    kbi_1.button(text='Product1', callback_data='product_buying')
    kbi_1.button(text='Product2', callback_data='product_buying')
    kbi_1.button(text='Product3', callback_data='product_buying')
    kbi_1.button(text='Product4', callback_data='product_buying')
    kbi_1.adjust(4)
    await message.answer('Выберите продукт для покупки:', reply_markup=kbi_1.as_markup())


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
