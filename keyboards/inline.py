from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Адрес 1️⃣",callback_data='addresses_1'),
        InlineKeyboardButton(text='Адреc 2️⃣',callback_data='addresses_2'),
        InlineKeyboardButton(text='Адрес 3️⃣',callback_data='addresses_3'),
        InlineKeyboardButton(text='Адрес 4️⃣',callback_data='addresses_4'),
        width=2

    )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ютуб 🎥",url="https://www.youtube.com/watch?v=indnl_tBHpw"),
            InlineKeyboardButton(text="телеграм ✨",url="tg://resolve?domain=Rren239")
        ]

    ]
)