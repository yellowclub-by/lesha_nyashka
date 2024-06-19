from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline


user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("""Добро пожаловать в наш магазин молочной продукции! 🥛🧀 
Мы рады видеть вас здесь! В нашем ассортименте вы найдете самые свежие и качественные молочные продукты, 
включая молоко (свежее, пастеризованное, ультрапастеризованное), сыры (твердые, мягкие, рассольные),  кефир 
(натуральныq и с добавками), творог и многое другое! 
Чтобы сделать заказ, просто выберите интересующие вас товары из меню. Если у вас возникнут вопросы, не стесняйтесь 
обращаться к нашему поддержке — мы всегда готовы помочь! Спасибо, что выбрали нас! Приятных покупок! 😊""",reply_markup=reply.start_kb)


@user_router.message(F.text.lower() == "меню 📖")
@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("вот наше меню",reply_markup=reply.menu_kb)


@user_router.message(F.text.lower() == "о нас 👥")
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("бот для продажи молочной продукции",reply_markup=inline.links_kb)


@user_router.message(F.text.lower() == "контакты 🎮")
@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("Лёша +375 29 228 228")


@user_router.message(F.text.lower() == "адрес 🅿️")
@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Наш адрес ", reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_types(callback: types.CallbackQuery):
    await callback.answer()
    querry = callback.data.split('_')[1]
    await callback.message.delete()
    if querry == "1":
        await callback.message.answer("первый адрес")
    elif querry == "2":
        await callback.message.answer('второй адрес')
    elif querry == '3':
        await callback.message.answer('третий адрес')
    elif querry == '4':
        await callback.message.answer('четвёртый адрес')


@user_router.message(F.text.lower() == "назад 🚫")
async def back_home(message: types.Message):
    await message.answer("главное меню", reply_markup=reply.start_kb)


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

