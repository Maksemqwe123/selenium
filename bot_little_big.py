from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from button import user_game, user_game_param
from aiogram.dispatcher.filters import Text
import logging
import os
import aiofiles
import random


number = random.randint(1, 15)
param = random.choice(['Орёл', 'Решка'])
count_of_attempts = 1
count = 1
print(number)

bot = Bot('5958293925:AAGh2IVIUkvGfygLO-ebFbIzU-r0QfZJnAA')
dp = Dispatcher(bot)

users = dict()


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await message.answer(f'В какую вы игру хотите сыграть ?', reply_markup=user_game)


@dp.message_handler(Text(equals='Больше-Меньше', ignore_case=True))
async def start_game_little_big(message: types.Message):
    global count_of_attempts

    if str(message.from_user.id) not in users.keys():
        users[str(message.from_user.id)] = message.from_user.full_name

        async with aiofiles.open('users_data.txt', 'w+') as users_file:
            for ID, username in users.items():
                await users_file.write(f'ID: {ID} | Username: {username}')

    if count_of_attempts == 1:
        await message.answer(f'Привет, я загадал число от 1 до 15, попробуй его угадать😉')
    else:
        await message.answer(f'Введите число🧐')


@dp.message_handler(Text(equals='орёл или решка', ignore_case=True))
async def start_game_param(message: types.Message):
    global count_of_attempts

    if count_of_attempts == 1:
        await message.answer('Я бросил монетку🪙: орёл или решка?', reply_markup=user_game_param)
    else:
        await message.answer(f'Введите ответ орел или решка🧐', reply_markup=user_game_param)


@dp.message_handler(Text(equals='Орёл', ignore_case=True))
async def info_param(message: types.Message):
    global param, count_of_attempts

    if str(message.text) == param:
        await message.answer(f'\nВы угадали!🎉\nВы потратили {count} попытку\попыток', reply_markup=user_game)
    else:
        await message.answer('Вы не угадали, попробуйте ещё раз🙃')
        count_of_attempts += 1


@dp.message_handler(Text(equals='Решка', ignore_case=True))
async def info_param(message: types.Message):
    global param, count_of_attempts

    if str(message.text) == param:
        await message.answer(f'\nВы угадали!🎉\nВы потратили {count} попытку\попыток', reply_markup=user_game)
    else:
        await message.answer('Вы не угадали, попробуйте ещё раз🙃')
        count_of_attempts += 1


@dp.message_handler()
async def info(message: types.Message):
    global number, count_of_attempts

    try:
        if int(message.text) == number:
            await message.answer(f'Вы угадали!🎉\nКоличество попыток: {count_of_attempts}', reply_markup=user_game)

        elif int(message.text) < number:
            await message.answer(f'Введенное число меньше загаданного🙃')
            count_of_attempts += 1
        else:
            await message.answer(f'Введенное число больше загаданного🙃')
            count_of_attempts += 1
    except:
        print(13)

if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)