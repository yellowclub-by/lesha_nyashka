from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Адрес_1",callback_data='addresses_1'),
        InlineKeyboardButton(text='Адрес_2',callback_data='addresses_2'),
        InlineKeyboardButton(text='Адрес_3',callback_data='addresses_3'),
        InlineKeyboardButton(text='Адрес_4',callback_data='addresses_4'),
        width=2

    )
    return builder.as_markup()