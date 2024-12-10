from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from bot.keyboards.inline import settings_kb
from database.models import Users

router = Router()


@router.callback_query(F.data == "settings")
async def user_settings(call: CallbackQuery, i18n: I18nContext, user: Users) -> None:
    await call.message.edit_caption(caption=i18n.settings(box_size=user.box_size,
                                                          border=user.border,
                                                          fill_color=user.fill_color,
                                                          back_color=user.back_color,
                                                          file_format=user.file_format),
                                    reply_markup=settings_kb)