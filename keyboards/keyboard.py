from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu():
    buttons = [
        [
            InlineKeyboardButton(text='📱 Телефоны и ⌚ гаджеты', callback_data='phone_gadget'),
            InlineKeyboardButton(text='🏠 Бытовая техника', callback_data='appliances')
         ],
        [
            InlineKeyboardButton(text='🔊 Аудио, 📹 Видео', callback_data='periphery'),
            InlineKeyboardButton(text='💻 Компьютеры', callback_data='comp')
        ],
        [
            InlineKeyboardButton(text='📺 Телевизоры', callback_data='tv'),
            InlineKeyboardButton(text='🧰 Строительсто и ремонт', callback_data="sport")
        ],
        [
            InlineKeyboardButton(text='⬇️ Еще', callback_data='more')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
