from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='Адрес')
        ],
        [
            KeyboardButton(text='Контакты'),
            KeyboardButton(text='О нас')
        ]
    ],

    resize_keyboard=True,
    input_field_placeholder='Что вы хотите увидеть?'

)
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='моржёное'),
            KeyboardButton(text='сыр'),
            KeyboardButton(text='тварог')
        ],
        [
            KeyboardButton(text='сырки'),
            KeyboardButton(text='молоко'),
            KeyboardButton(text='кефир')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вы хотите увидеть?'
)