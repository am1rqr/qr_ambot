from aiogram_i18n import LazyProxy
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=LazyProxy("settings_button"), callback_data="settings")
    ],
    [
        InlineKeyboardButton(text=LazyProxy("channel_button"), url="https://t.me/automium")
    ]
])