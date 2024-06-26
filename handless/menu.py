from aiogram import types, Router, F
from aiogram.types import FSInputFile

menu_router = Router()


@menu_router.message(F.text.lower() == "мороженое 🍧")
async def menu_ice_cream(message: types.Message):
    photo = FSInputFile('images\menu\мороженое.jpg')
    await message.answer_photo(photo, caption="""<b>Мороженое "Гомельское" </b>

Вес 250/ 375/ 500 мг
Вкусы: Шоколадный, Малиновый, Вишня

Цена 0,50 руб за 125 мг""")

@menu_router.message(F.text.lower() == "сырки 🍫")
async def menu_sirki(message: types.Message):
    photo = FSInputFile('images\menu\сырки.jpg')
    await message.answer_photo(photo, caption="""<b>Сырки "Гомельские" </b>

Вес 125/ 250/ 350 мг
Вкусы: Шоколадный, Малиновый, Вишня

Цена 0,50 руб за 125 мг""")

@menu_router.message(F.text.lower() == "молоко 🥛")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\молоко.jpg')
    await message.answer_photo(photo, caption="""<b>Молоко классическое</b> 

Адрес производства Минский молочный завод
Объём 0,5 / 1 / 2 литра 
Проценты жира 3 / 5 / 10 %

Цена 0,75 руб за 500 мл""" )

@menu_router.message(F.text.lower() == "сыр 🧀")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\сыр.png')
    await message.answer_photo(photo, caption="""<b>Сыр Кобринский</b>
    
Адрес производства Кобринский сырзавод
Вес до 15 кг

Цена 1 руб за 500 мг""")

@menu_router.message(F.text.lower() == "творог 🪨")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\творог.jpg')
    await message.answer_photo(photo, caption="""<b>Творог "Фермерский"</b>
    
Адрес производства Минский творожный завод
Вес 0,5 / 1 / 2 кг 
Проценты жира 3 / 5 / 10 %

Цена 1,25 руб за 500 мг""")

@menu_router.message(F.text.lower() == "кефир 🍼")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\кефир.png')
    await message.answer_photo(photo, caption="""<b>Кефир "Минский"</b>
    
Адрес производства Минский молочный завод
Объём 0,5 / 1 / 2 л
Проценты жира 3 / 5 / 10 %

Цена 1,25 руб за 500 мл""")