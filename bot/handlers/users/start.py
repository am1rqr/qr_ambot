from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram_i18n import I18nContext

from bot.filters import IsPrivate
from bot.keyboards.inline import menu_kb

router = Router()


@router.message(IsPrivate(), CommandStart())
async def cmd_start(message: Message, i18n: I18nContext) -> None:
    await message.answer(i18n.menu(),
                         reply_markup=menu_kb)


@router.callback_query(F.data == "menu")
async def call_menu(call: CallbackQuery, i18n: I18nContext) -> None:
    await call.message.edit_caption(caption=i18n.menu(),
                                   reply_markup=menu_kb)