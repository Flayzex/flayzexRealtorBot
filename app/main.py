import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import Config
from handlers import router


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


async def main():
    logger.info("🚀 Бот запускается...")

    bot = Bot(token=Config.BOT_API)
    dp = Dispatcher()

    dp.include_router(router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("✅ Вебхук удалён (если был), начинаем поллинг...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(f"❌ Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()
        logger.info("🛑 Бот остановлен.")


if __name__ == "__main__":
    asyncio.run(main())
