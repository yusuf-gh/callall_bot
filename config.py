from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command


# -1002422035606
API_TOKEN = '7898591490:AAGJ3EEkeooqYXfRQSVkgD2SxOpQc4Qq5M0'
ERRORS_GROUP_ID = -4587996370

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()


@router.message(Command(commands=['tagall']))
async def tag_all_members(message: types.Message):

    members = await bot.get_chat_administrators(message.chat.id)
    text = "Отмечаю всех администраторов:\n"


    try:
        for member in members:
            user = member.user
            if not user.is_bot:
                text += f"@{user.username or user.full_name}\n"


        await message.reply(text)

    except Exception as e:
        await bot.send_message(ERRORS_GROUP_ID,
                               f"Ошибка: {e}")




