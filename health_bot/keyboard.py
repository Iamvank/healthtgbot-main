from aiogram import types

def start_keyboard():
    """Клавиатура для команды /start"""
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Саморазвитие"), types.KeyboardButton(text="Биохакинг")]
        ],
        resize_keyboard=True,  # Параметр для изменения размера
        one_time_keyboard=False
    )
    return keyboard

def self_development_keyboard():
    """Клавиатура для выбора подкатегории саморазвития"""
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Мотивация"),
             types.KeyboardButton(text="Навыки"),
             types.KeyboardButton(text="Цели")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def biohacking_keyboard():
    """Клавиатура для выбора подкатегории биохакинга"""
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Здоровье"),
             types.KeyboardButton(text="Продуктивность"),
             types.KeyboardButton(text="Питание")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def psychology_keyboard():
    """Клавиатура для выбора подкатегории психологии"""
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Эмоции"),
             types.KeyboardButton(text="Отношения"),
             types.KeyboardButton(text="Мозг")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard
