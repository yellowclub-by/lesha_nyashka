import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "7125759779:AAFJ8kSj09MrCSwlqRy_zyNtSwqObRiMNbA"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("ЗДРАСТВУЙТЕ ПЕРЕД ВАМИ БОТ МОЛО КО КО КО СОЗДАНЫЙ ЛЁШЕЙ НЯШКОЙ")


@dp.message()
async def echo(message: types.Message):
    # await message.answer("бот в разработке")
    user_text = message.text
    await message.answer(message.text)


async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
