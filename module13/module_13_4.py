from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio


api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['calories'])
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
    await message.answer('Если хотите получить информацию о ваших калорийных потреблениях, введите /calories')
    await state.finish()


@dp.message_handler

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /calories, чтобы рассчитать норму калорий.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
