from aiogram.fsm.state import State, StatesGroup


class ChangeSize(StatesGroup):
    size = State()