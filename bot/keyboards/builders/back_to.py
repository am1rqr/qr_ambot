from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext


def back_to_builder(callback_data: str, i18n: I18nContext) -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text=i18n.back_button(), callback_data=callback_data)

    return keyboard_builder.as_markup()
