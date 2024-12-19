from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from conf import TOKEN
from crud_functions import *
import asyncio

api = TOKEN
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
button3 = KeyboardButton(text = 'Купить')
button4 = KeyboardButton(text = 'Регистрация')
kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(button, button2).add(button3).add(button4)

inline_kb = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')
)

product_kb = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Product1', callback_data='product_buying'),
    InlineKeyboardButton(text='Product2', callback_data="product_buying"),
    InlineKeyboardButton(text='Product3', callback_data="product_buying"),
    InlineKeyboardButton(text='Product4', callback_data="product_buying")
)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text='Регистрация')
async def sign_up(message: types.Message):
    initiate_db()
    await message.answer('Введите имя пользователя (только латинский алфавит): ')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Вы отправили не число')
        return
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Пользователь успешно зарегистрирован!')
    await state.finish()



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Это бот для расчета калорий. Чтобы начать, выбери действие')
    await message.answer('Выберите действие:', reply_markup=kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in get_all_products():
        number = i[0]
        title = i[1]
        description = i[2]
        price = i[3]
        await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
        num = str(number)
        with open(f'files/{num}.webp', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=product_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(f'Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text='Рассчитать')
async def maim_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула для рассчета калорий для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: UserState):
    if not message.text.isdigit():
        await message.answer('Вы отправили не число')
        return
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в сантиметрах')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: UserState):
    if not message.text.isdigit():
        await message.answer('Вы отправили не число')
        return
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес в килограммах')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: UserState):
    if not message.text.isdigit():
        await message.answer('Вы отправили не число')
        return
    await state.update_data(weight=message.text)
    data = await state.get_data()
    weight = float(data['weight'])
    growth = float(data['growth'])
    age = float(data['age'])
    calories_man = 10 * weight + 6.25 * growth - 5 * age + 5
    calories_woman = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Ваша нормальная масса тела м - {calories_man} калорий.')
    await message.answer(f'Ваша нормальная масса тела ж - {calories_woman} калорий.')
    await message.answer('Введите /start.')
    await state.finish()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Я Вас не понимаю. Для начала взаимодействия введите команду /start и выберите действие.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
