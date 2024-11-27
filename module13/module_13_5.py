from pydoc import text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from conf import TOKEN
import asyncio

api = TOKEN
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(button, button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Это бот для расчета калорий. Чтобы начать, выбери действие')
    await message.answer('Выберите действие:', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    text = message.text.lower()
    await message.answer('Введите свой возраст')
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


@dp.message_handler

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start и выберите действие.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
