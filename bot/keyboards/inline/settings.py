from aiogram_i18n import LazyProxy
from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton


settings_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=LazyProxy("box_size_button"), callback_data="size#box_size"),
        InlineKeyboardButton(text=LazyProxy("border_button"), callback_data="size#border")
    ],
    [
        InlineKeyboardButton(text=LazyProxy("fill_color_button"), callback_data="color#fill"),
        InlineKeyboardButton(text=LazyProxy("back_color_button"), callback_data="color#back")
    ],
    [
        InlineKeyboardButton(text=LazyProxy("file_format_button"), callback_data="file_format")
    ],
    [
        InlineKeyboardButton(text=LazyProxy("back_button"), callback_data="menu")
    ]
])