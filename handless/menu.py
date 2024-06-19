from aiogram import types, Router, F
from aiogram.types import FSInputFile

menu_router = Router()


@menu_router.message(F.text.lower() == "мороженое 🍧")
async def menu_ice_cream(message: types.Message):
    photo = FSInputFile('images\menu\мороженое.jpg')
    await message.answer_photo(photo, caption="ГООООООЙсмияыДААААА")

@menu_router.message(F.text.lower() == "сырки 🍫")
async def menu_sirki(message: types.Message):
    photo = FSInputFile('images\menu\сырки.jpg')
    await message.answer_photo(photo, caption="ГООООООЙяыквпчрасДААААА")

@menu_router.message(F.text.lower() == "молоко 🥛")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\молоко.jpg')
    await message.answer_photo(photo, caption="""<b>Молоко классическое</b> 
    Объём 0,5 / 1 / 2 литра 
    Цена 0,75 руб за 500 мл"""  )

@menu_router.message(F.text.lower() == "сыр 🧀")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\сыр.png')
    await message.answer_photo(photo, caption="")

@menu_router.message(F.text.lower() == "тварог 🪨")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\творог.jpg')
    await message.answer_photo(photo, caption="ГОварвар")

@menu_router.message(F.text.lower() == "кефир 🍼")
async def menu_milk(message: types.Message):
    photo = FSInputFile('images\menu\кефир.png')
    await message.answer_photo(photo, caption="ГОварлвар")