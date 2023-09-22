from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton, CallbackQuery
)

from config_read import config
from db.sqlite import insert_product

router = Router()


class Product(StatesGroup):
    choose_category = State()
    choose_name = State()
    choose_price = State()
    choose_characteristics = State()
    choose_photo = State()


def get_tool():
    button = [
        [InlineKeyboardButton(text="Добавить новый продукт", callback_data="edit_product")]
    ]

    return InlineKeyboardMarkup(inline_keyboard=button)


def get_catalog():
    buttons = [
        [
            InlineKeyboardButton(text='📱 Телефоны и ⌚ гаджеты', callback_data='choose_phone_gadgets'),
            InlineKeyboardButton(text='🏠 Бытовая техника', callback_data='choose_appliances')
        ],
        [
            InlineKeyboardButton(text='🔊 Аудио, 📹 Видео', callback_data='choose_periphery'),
            InlineKeyboardButton(text='💻 Компьютеры', callback_data='choose_computers')
        ],
        [
            InlineKeyboardButton(text='📺 Телевизоры', callback_data='edit_tv'),
            InlineKeyboardButton(text='🧰 Строительсто и ремонт', callback_data="choose_tools")
        ],
        [
            InlineKeyboardButton(text='⬇️ Еще', callback_data='more')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def get_catalog_phone():
    buttons = [
        [
            InlineKeyboardButton(text='📱 Смартфоны', callback_data='edit_phone'),
            InlineKeyboardButton(text='⌚ Смарт часы', callback_data='edit_watch')
        ],
        [
            InlineKeyboardButton(text='🔌 Адаптеры', callback_data='edit_charger'),
            InlineKeyboardButton(text='📲 Чехлы', callback_data="edit_case")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def isAdmin(user_id):
    return user_id == int(config.admin_id.get_secret_value())


@router.message(Command("admin"))
async def admin(message: Message):
    if isAdmin(message.from_user.id):
        await message.answer(text="Админский режим:", reply_markup=get_tool())
    else:
        await message.answer("Ваш запрос неверный")

@router.callback_query(F.data == "edit_product")
async def choose_catalog(callback: CallbackQuery):
    await callback.message.answer(text="Выберите категорию продукта:", reply_markup=get_catalog())
    await callback.answer()


@router.callback_query(F.data.startswith("choose"))
async def choose_catalog(callback: CallbackQuery):
    if callback.data.endswith("phone_gadget"):
        await callback.message.answer(text="Выберите категорию продукта:", reply_markup=get_catalog_phone())
    await callback.answer()


@router.callback_query(F.data.startswith("edit"))
async def choose_sub_catalog(callback: CallbackQuery, state: FSMContext):
    if callback.data.endswith("phone"):
        await state.update_data(choose_category="phones")
        await callback.message.answer(text="Добавление нового телефона...\nВведите имя")
    elif callback.data.endswith("watch"):
        await state.update_data(choose_category="watch")
        await callback.message.answer(text="Пока что тут ничего нету :(")
    await state.set_state(Product.choose_name)
    await callback.answer()


@router.message(Product.choose_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(choose_name=message.text)
    await message.answer(text="Укажите цену: ")
    await state.set_state(Product.choose_price)


@router.message(Product.choose_price)
async def get_price(message: Message, state: FSMContext):
    await state.update_data(choose_price=message.text)
    await message.answer(text="Напишите описание товара: ")
    await state.set_state(Product.choose_characteristics)


@router.message(Product.choose_characteristics)
async def get_characteristics(message: Message, state: FSMContext):
    await state.update_data(choose_characteristics=message.text)
    await message.answer(text="Отправьте фото")
    await state.set_state(Product.choose_photo)


@router.message(Product.choose_photo)
async def get_photo(message: Message, state: FSMContext):
    await state.update_data(choose_photo=message.photo[-1].file_id)
    product = await state.get_data()
    await message.answer("Поздравляю все прошло успешно 🥳")
    await insert_product(product["choose_category"], product["choose_name"], product["choose_price"], product["choose_characteristics"], product["choose_photo"])
    await state.clear()

