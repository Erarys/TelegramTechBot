from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.phone_keyboard import get_catalog_phones, get_catalog_brands
from db.sqlite import select_product

router = Router()


@router.callback_query(F.data == "phone_gadget")
async def phones(callback: CallbackQuery):
    await callback.message.answer(
        "Раздел: Смартфонов и гаджетов",
        reply_markup=get_catalog_phones()
    )
    await callback.answer()


@router.callback_query(F.data == "phone")
async def phones_brands(callback: CallbackQuery):
    await callback.message.answer(
        text="Смартфоны",
        reply_markup=get_catalog_brands()
    )
    await callback.answer()


@router.callback_query(F.data == "iphone")
async def iphone(callback: CallbackQuery):
    res = await select_product()
    for phone in res:
        await callback.message.answer_photo(phone[4], caption="{}\nЦена{}\n{}".format(phone[1], phone[2], phone[3]))