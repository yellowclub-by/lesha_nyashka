from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline


user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("""Добро пожаловать в наш магазин молочной продукции! 🥛🧀 
Мы рады видеть вас здесь! В нашем ассортименте вы найдете самые свежие и качественные молочные продукты, 
включая молоко (свежее, пастеризованное, ультрапастеризованное), сыры (твердые, мягкие, рассольные),  кефир 
(натуральные и с добавками), творог и многое другое! 
Чтобы сделать заказ, просто выберите интересующие вас товары из меню. Если у вас возникнут вопросы, не стесняйтесь 
обращаться к нашему поддержке — мы всегда готовы помочь! Спасибо, что выбрали нас! Приятных покупок! 😊""",reply_markup=reply.start_kb)


@user_router.message(F.text.lower() == "меню 📖")
@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("вот наше меню",reply_markup=reply.menu_kb)


@user_router.message(F.text.lower() == "о нас 👥")
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("""Привет! Добро пожаловать в наш бот по продаже молочной продукции! 🥛🧀

Здесь вы найдете широкий ассортимент свежих и натуральных молочных продуктов, включая молоко, творог, сыр, йогурты и многое другое. Наши продукты изготовлены из высококачественного молока и не содержат искусственных добавок.
### Как пользоваться ботом:
1. **Меню**: Просмотрите наш ассортимент и выберите интересующие вас товары.
2. **Адреса**: Узнайте где можно забрать заказ.
3. **Контакты**: Если у вас возникнут вопросы, наша служба поддержки всегда готова помочь.
Начните с выбора категории продукции, и мы с радостью поможем вам найти всё, что нужно для вашего стола. Приятных покупок! 🛒
Если у вас есть вопросы или предложения, не стесняйтесь писать нам.""",reply_markup=inline.links_kb)


@user_router.message(F.text.lower() == "контакты 🎮")
@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("""Если у вас возникнут вопросы, наша служба поддержки всегда готова помочь
Номер службы поддержки +375 29 228 228""")


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
        await callback.message.answer("https://www.google.com/maps/place/%D0%9F%D0%B0%D1%80%D0%B8%D0%BA%D0%BC%D0%B0%D1%85%D0%B5%D1%80%D1%81%D0%BA%D0%B0%D1%8F/@53.9192198,27.4962562,17z/data=!4m10!1m2!2m1!1z0YPQu9C40YbQsCDQv9GD0YjQutC40L3QsCDQtNC-0Lwg0LrQvtC70L7RgtGD0YjQutC40L3QsA!3m6!1s0x46dbc54037faaaab:0x127533662bf58a52!8m2!3d53.9190887!4d27.4984782!15sCjfRg9C70LjRhtCwINC_0YPRiNC60LjQvdCwINC00L7QvCDQutC-0LvQvtGC0YPRiNC60LjQvdCwkgEKaGFpcl9zYWxvbuABAA!16s%2Fg%2F1hc7gcvl0?entry=ttu")
    elif querry == "2":
        await callback.message.answer('https://www.google.com/maps/place/%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9+%D0%BC%D0%BE%D0%BB%D0%BE%D1%87%D0%BD%D1%8B%D0%B9+%D0%B7%D0%B0%D0%B2%D0%BE%D0%B4+%E2%84%96+1/@53.9008964,27.6379313,16z/data=!4m10!1m2!2m1!1z0LzQvtC70L7Rh9C90LDRjyDQv9GA0L7QtNGD0LrRhtC40Y8g0LHQtdC70LDRgNGD0YHRjA!3m6!1s0x46dbce66b8795643:0xfd41550008e9c51e!8m2!3d53.9007974!4d27.6459877!15sCjTQvNC-0LvQvtGH0L3QsNGPINC_0YDQvtC00YPQutGG0LjRjyDQsdC10LvQsNGA0YPRgdGMWjYiNNC80L7Qu9C-0YfQvdCw0Y8g0L_RgNC-0LTRg9C60YbQuNGPINCx0LXQu9Cw0YDRg9GB0YySAQ5kYWlyeV9zdXBwbGllcpoBJENoZERTVWhOTUc5blMwVkpRMEZuU1VONU1GazJOek5uUlJBQuABAA!16s%2Fg%2F11bv1mpn_h?entry=ttu')

    await callback.answer()

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

