from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from bot.keyboards.builders import back_to_builder
from bot.states.users import ChangeSize

router = Router()


@router.callback_query(F.data.startswith("size#"))
async def change_qr_size(call: CallbackQuery, i18n: I18nContext, state: FSMContext):
    change_type = call.data.split("#")[1]
    await state.update_data(change_type=change_type)

    await call.message.edit_caption(caption=i18n.change_size(change_type),
                                    reply_markup=back_to_builder("settings", i18n))
    await state.set_state(ChangeSize.size)