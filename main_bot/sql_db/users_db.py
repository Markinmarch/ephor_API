import logging


from .bot_tables import Bot_tables_DB


class Users(Bot_tables_DB):

    '''
    Класс наследует основной класс :Bot_tables_DB:
    для реализации БД. Данный класс реализован с
    целью управления таблицей :users: по методу CRUD
    '''

    def insert_users(
        self,
        user_id: int,
        user_name: str
    ) -> None:
        self.cur.execute(
            '''
            INSERT INTO users (
                id,
                user_name
            )
            VALUES (?, ?);            
            ''',
            (
                user_id,
                user_name
            )
        )
        self.conn.commit()
        logging.info(f'New user -- id: {user_id} -- name: {user_name} -- has been added')

    def select_name(
        self,
        user_id: int
    ) -> tuple:
        self.cur.execute(
            '''
            SELECT user_name FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        return self.cur.fetchone()

    def checking_users(
        self,
        user_id: int
    ) -> bool:
        self.cur.execute(
            '''
            SELECT COUNT(*) FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        return self.cur.fetchone()[0]
    
    def select_all_data(self):
        self.cur.execute(
            '''
            SELECT * FROM users
            '''
        )
        return self.cur.fetchall()

    def delete_users(
        self,
        user_id: int
    ) -> None:
        self.cur.execute(
            '''
            DELETE FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        self.conn.commit()
        logging.info(f'User {user_id} deleted')


users = Users()