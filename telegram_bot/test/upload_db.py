import unittest
import random
import time


from telegram_bot.sql_db.users_db import users
from telegram_bot.sql_db.posts_db import posts
from telegram_bot.sql_db.responders_db import responders


random_names = ['Евгений', 'Пётр', 'Василий', 'Андрей', 'Валерий', 'Фёдор', 'Алексей', 'Александр', 'Сергей']

class TestCaseDB:

    def __init__(
        self,
        user_id,
        user_name,
        user_age,
        user_gender,
        user_phone,
        message_id
    ) -> None:
        self.id = user_id
        self.name = user_name
        self.age = user_age
        self.gender = user_gender
        self.phone = user_phone
        self.msgid = message_id
        
    def upload_users(self) -> None:
        users.insert_users(
            user_id = self.id,
            user_name = self.name,
            user_age = self.age,
            user_gender = self.gender,
            user_phone = self.phone
        )

    def upload_posts(self) -> None:
        posts.insert_post(
            post_id = self.msgid,
            user_id = self.id
        )

    def upload_respond(self) -> None:
        responders.respond_post(
            responder_id = self.id,
            post_id = self.msgid
        )

def randomizer() -> list:
    random_id = random.randrange(1000000, 9999999, 1)
    random_name = random.choice(random_names)
    random_age = random.randrange(18, 50, 1)
    random_gender = random.randrange(0, 1, 1)
    random_phone = int('7978' + str(random.randrange(1000000, 9999999, 1)))
    random_msgid = random.randrange(100, 999999, 1)
    random_lst = [
        random_id,
        random_name,
        random_age,
        random_gender,
        random_phone,
        random_msgid
    ]
    return random_lst

def get_upload_DB(lst):
    upload_db = TestCaseDB(
        lst[0],
        lst[1],
        lst[2],
        lst[3],
        lst[4],
        lst[5]
    )
    upload_db.upload_users()
    upload_db.upload_posts()
    upload_db.upload_respond()
        
start_time = time.time()
while True:
    if len(users.select_all_data()) != 100:
        get_upload_DB(randomizer())
        continue
    break
print(f'--- {time.time() - start_time} ---')

# print(len(users.select_all_data()))
