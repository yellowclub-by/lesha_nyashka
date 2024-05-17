from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("ЗДРАСТВУЙТЕ ПЕРЕД ВАМИ БОТ МОЛО КО КО КО СОЗДАНЫЙ ЛЁШЕЙ НЯШКОЙ")

@user_router.message(F.text.lower() == "меню")
@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("вот наше меню")

@user_router.message(F.text.lower() == "о нас")
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("бот для продажи молочной продукции")

@user_router.message(F.text.lower() == "контакты")
@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("Лёша +375 29 228 228")

@user_router.message(F.text.lower() == "адрес")
@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Наш адрес ")


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == "доставка")
# @user_router.message(F.text.lower().contains("достав"))
# @user_router.message(F.text.lower().startswith("как"))
# @user_router.message(F.text.lower().endswith("?"))
# @user_router.message(F.text.lower().startswith("как"), F.text.lower().endswith("?"))
# @user_router.message((F.text.lower().contains("цен")) | (F.text.lower().contains("стоимост")))
async def echo(message: types.Message):
    await message.answer("сработал магический фильтр")
