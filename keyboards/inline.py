from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="проспект Пушкина 66, Минск",callback_data='addresses_1'),
        InlineKeyboardButton(text='улица Солтыса 185, Минск',callback_data='addresses_2'),
        width=1

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