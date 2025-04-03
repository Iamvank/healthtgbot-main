from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import logging
import asyncio
from config import TOKEN  # Импортируем токен из config.py
from keyboard import start_keyboard, self_development_keyboard, biohacking_keyboard, psychology_keyboard  # Импортируем клавиатуры

# Инициализация
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Обработчик команды /start
@dp.message()
async def cmd_start(message: Message):
    if message.text == "/start":
        keyboard = start_keyboard()
        await message.answer("Привет! Выберите категорию:", reply_markup=keyboard)

# Обработчик для категорий
@dp.message()
async def handle_category(message: Message):
    if message.text == "Саморазвитие":
        keyboard = self_development_keyboard()
        await message.answer("Выберите подкатегорию:", reply_markup=keyboard)
    elif message.text == "Биохакинг":
        keyboard = biohacking_keyboard()
        await message.answer("Выберите подкатегорию:", reply_markup=keyboard)
    elif message.text == "Психология":
        keyboard = psychology_keyboard()
        await message.answer("Выберите подкатегорию:", reply_markup=keyboard)
    else:
        await message.answer("Неизвестная категория.")

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
