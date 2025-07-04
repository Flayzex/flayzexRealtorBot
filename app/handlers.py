from aiogram import Router, types, F

from services.data_templating import data_templating


router = Router()

@router.message(F.text == "/start")
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Привет! Я Flayzex Realtor Bot — твой помощник в создании шаблонных текстов для объявлений о квартирах.\n\n"
        "🔧 Я помогу тебе быстро и грамотно оформить описание квартиры. Просто отправь данные в следующем формате:\n\n"
        "📍 *Район, Локация*\n"
        "🛏 *Количество комнат / Этаж / Этажность*\n"
        "📐 *Площадь в м²*\n"
        "💰 *Цена*\n"
        "🆔 *ID*\n\n"
        "_Пример:_\n"
        "Юнусабадский, метро Бадамзар\n"
        "3 4 9\n"
        "78\n"
        "78 000\n"
        "123456\n\n"
        "📨 После отправки такого сообщения я сгенерирую удобный шаблон, который ты сможешь использовать для публикации."
    )



@router.message()
async def templating_handler(message: types.Message):
    await message.answer(data_templating(message.text), parse_mode="HTML")