import os
import logging
import sqlite3


from core.config import DB_NAME, DB_PATH


class Bot_tables_DB:
    '''
    Класс реализует создание связанных между собой таблиц базы данных.
        :name: параметр наименования базы данных
        :path: параметр маршрута до папки с базой данных
        :conn: параметр реализует подключение к сессии БД
        :cur: параметр указателя БД
    '''

    def __init__(
            self,
            name_DB: str,
            path_DB: str
        ):
        self.name = name_DB
        self.path = path_DB
        self.conn = sqlite3.connect(f'{self.path}/{self.name}.db')
        self.cur = self.conn.cursor()

    def create_users_table(self) -> None:
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL
            );
            '''
        )
        self.conn.commit()
        logging.info('--- Table "USERS" has been created ---')

    def create_tasks_table(self) -> None:
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS tasks(
                msg_id INTEGER NOT NULL,
                child_msg_id INTEGER NOT NULL,
                chat_id INTEGET NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );            
            '''
        )
        self.conn.commit()
        logging.info('--- Table "TASKS" has been created ---')

    def drop_posts_table(self) -> None:
        self.cur.execute(
            '''
            DROP TABLE posts;
            '''
        )
        self.conn.commit()

    def create_responders_table(self) -> None:
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS responders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                responder_id INTEGER NOT NULL,
                post_id INTEGER NOT NULL,
                FOREIGN KEY (post_id) REFERENCES posts(id)
            );            
            '''
        )
        self.conn.commit()
        logging.info('--- Table "RESPONDERS" has been created ---')
