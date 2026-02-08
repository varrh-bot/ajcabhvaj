import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен вашего бота (получите у @BotFather)
BOT_TOKEN = '8532556951:AAHu0tM5HamXLby2dwSp-VFCwkKSaGDi3Ws'

# URL сайта
SURVEY_URL = 'https://surveyforall.surf/eazy'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    
    # Текст приветственного сообщения
    welcome_text = (
        "🌟 <b>Добро пожаловать!</b> 🌟\n\n"
        "Хотите получить <b>бесплатные звезды</b>? 🎁\n\n"
        "Участвуйте в простых опросах и зарабатывайте звезды, "
        "которые можно использовать в Telegram!\n\n"
        "✅ Быстрые опросы\n"
        "✅ Честные выплаты\n"
        "✅ Моментальное начисление звезд\n\n"
        "Нажмите кнопку ниже, чтобы начать! 👇"
    )
    
    # Создание инлайн-кнопки
    keyboard = [
        [InlineKeyboardButton("⭐ Принять участие!", url=SURVEY_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправка сообщения
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

def main() -> None:
    """Запуск бота"""
    
    # Создание приложения
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрация обработчика команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Запуск бота
    print("Бот запущен!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()