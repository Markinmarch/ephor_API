from aiogram.fsm.state import State, StatesGroup


class TasksForm(StatesGroup):
    user_id = State()
    automat_id = State()
    route_id = State()
    error = State()

class UsersForm(StatesGroup):
    name = State()
    phone = State()

class InspectionRouts(StatesGroup):
    user_ids: list = State()
