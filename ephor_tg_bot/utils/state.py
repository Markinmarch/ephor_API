from aiogram.fsm.state import State, StatesGroup


class UserForm(StatesGroup):
    name = State()

class TasksForm(StatesGroup):
    status = State()
    error = State()

class InspectionRouts(StatesGroup):
    user_ids: list = State()
