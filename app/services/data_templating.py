import logging
import re


def data_templating(data: str) -> str:
    if len(data.split("\n")) != 5:
        return 'Неправильный формат, введите /start для просмотра примера правильного ввода'
    PLACE, OPTIONS, AREA, PRICE, ID = data.split("\n")

    match_place = re.match(r"^(.+?,)(.+)$", PLACE)
    DISTRICT, LOCATION = match_place.group(1).strip(" ,"), match_place.group(2).strip(
        " "
    )

    match_options = re.findall(r"\d+", OPTIONS)
    ROOMS_AMOUNT, STOREY, STOREYS_AMOUNT = match_options

    result = f"""<strong>
Аренда квартиры🏠

📍Район:  {DISTRICT} район
📍Локация: {LOCATION}


🔹{ROOMS_AMOUNT} / {STOREY} / {STOREYS_AMOUNT}
🔹Площадь - {AREA} м²
🔹Мебель Техника✔️
🔹Депозит/Предоплата ✔️

💵Цена: {PRICE} у.е
🌀Срм #{ID} (Алим)

Для подробной информации:
💬 <a href="https://t.me/alim_expert">Администратор</a>

<a href="https://t.me/expert_arenda">🚀Аренда1</a><a href="https://t.me/EXPERT_RENT_UZ">🚀Аренда 2</a>
<a href="https://t.me/EXPERT_SALE_UZ">🚀Продажа</a> <a href="https://www.instagram.com/expert.real_estate?igsh=MXg2Y2x3aGp6a2F1aA%3D%3D&utm_source=qr">📷Инстаграм</a>
</strong>
"""

    return result
