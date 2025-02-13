from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command

# 🔑 Токены
API_TOKEN = API_TELEGRAM_BOT
ERRORS_GROUP_ID = GROUP_ID  # Группа для логирования ошибок

# 🚀 Инициализация бота
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
router = Router()

# 🔧 Устанавливаем API-ключ OpenAI
openai.api_key = OPENAI_API_KEY

# 🎭 Функция для генерации ответа OpenAI
def get_poetic_response(user_request: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a poetic butler named Sebastian in a Telegram group."},
                {"role": "user", "content": user_request}
            ],
            max_tokens=100
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Ошибка OpenAI: {str(e)}"

# 🏷 Хэндлер для команды /tagall (отмечает всех админов)
@router.message(Command("tagall"))
async def tag_all_members(message: types.Message):
    try:
        members = await bot.get_chat_administrators(message.chat.id)
        text = "📢 Отмечаю всех участников:\n"

        for member in members:
            user = member.user
            if not user.is_bot:
                text += f"{user.mention_html()}\n"

        await message.reply(text, parse_mode=ParseMode.HTML)

    except Exception as e:
        await bot.send_message(ERRORS_GROUP_ID, f"Ошибка: {e}")

# 🤖 Хэндлер для реакции на "Себастьян"
@router.message(F.text.lower().contains("cебастьян"))
async def respond_to_sebastian(message: types.Message):
    user_text = message.text.split("Себастьян", 1)[-1].strip()

    if user_text:
        poetic_response = get_poetic_response(user_text)
        await message.reply(f"📜 {poetic_response}")
    else:
        await message.reply("🧐 Я вас слушаю, но не понял вопроса. Как мне помочь?")

# 🔗 Подключаем router к Dispatcher
dp.include_router(router)

# 🚀 Функция запуска бота
async def main():
    await dp.start_polling(bot)

# 🔥 Запуск бота
if __name__ == "__main__":
    asyncio.run(main())


