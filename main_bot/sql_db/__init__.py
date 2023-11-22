import logging
import os


from . import bot_tables
from . import tasks_db
from . import users_db
from core.config import DB_NAME, DB_PATH


DB_tables = bot_tables.Bot_tables_DB(DB_NAME, DB_PATH)
logging.info('--- Database for "SevCoffeeService BOT" has been created ---')

if DB_NAME + '.db' not in os.listdir(DB_PATH) or os.path.isdir(DB_PATH) == False:
    DB_tables.create_users_table()
    DB_tables.create_tasks_table()
else:
    logging.info('--- Database for "SevCoffeeService" connection established ---')

tasks = tasks_db.Tasks()
users = users_db.Users()
