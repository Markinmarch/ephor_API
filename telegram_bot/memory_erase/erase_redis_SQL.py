# import redis
# import threading


# from telegram_bot.settings.config import REDIS_BD, REDIS_HOST, REDIS_PORT, DAY
# from telegram_bot.sql_db.bot_tables import Bot_tables_DB


# class EraseDataBases(Bot_tables_DB):

#     def __init__(self) -> None:
#         self.host = REDIS_HOST,
#         self.port = REDIS_PORT,
#         self.db = REDIS_BD

#     def erase_databases(self):
#         # очищаем redis
#         redis_db = redis.Redis(
#             host = self.host,
#             port = self.port,
#             db = self.db,
#         )
#         redis_db.flushdb(
#             asynchronous = True
#         )
#         # очищаем SQL
#         self.drop_responders_table()
#         self.drop_posts_table()

# def timer_to_erase():
#     timer = threading.Timer(
#         interval = DAY,
#         function = EraseDataBases.erase_databases()
#     )
#     timer.start()

