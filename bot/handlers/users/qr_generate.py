from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.types import Message, BufferedInputFile
from aiogram_i18n import I18nContext

from bot.filters import IsPrivate
from bot.keyboards.inline import menu_kb
from bot.utils.qr_generator import generate_qr
from database.models import Users

router = Router()


@router.message(IsPrivate(), F.content_type == ContentType.TEXT)
async def process_generate_qr(message: Message, i18n: I18nContext, user: Users) -> None:
    buffer = generate_qr(message.text, user.box_size, user.border,
                         user.fill_color, user.back_color, user.file_format)

    await message.reply_document(BufferedInputFile(buffer, filename=f"qrcode.{user.file_format}"))
    await message.answer_photo(photo=BufferedInputFile(buffer, filename=f"qrcode.{user.file_format}"),
                               caption=f"<i>{message.text}</i>",
                               reply_markup=menu_kb)
