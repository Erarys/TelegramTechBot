from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_catalog_phones():
    buttons = [
        [
            InlineKeyboardButton(text='📱 Смартфоны', callback_data='phone'),
            InlineKeyboardButton(text='⌚ Смарт часы', callback_data='watch')
        ],
        [
            InlineKeyboardButton(text='🔌 Адаптеры', callback_data='charger'),
            InlineKeyboardButton(text='📲 Чехлы', callback_data="case")
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_catalog_brands():
    buttons = [
        [
            InlineKeyboardButton(text="iPhone", callback_data="iphone"),
            InlineKeyboardButton(text="Samsung", callback_data="samsung")
        ],
        [
            InlineKeyboardButton(text="Показать", callback_data="show_phone")
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
