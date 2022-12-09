import random

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_game = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton('больше-меньше'),
    KeyboardButton('орёл или решка')
)

user_game_param = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Решка'),
    KeyboardButton('Орёл')
)