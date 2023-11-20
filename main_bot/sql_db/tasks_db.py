import logging


from main_bot.sql_db.bot_tables import Bot_tables_DB


class Tasks(Bot_tables_DB):

    def take_task(
        self,
        msg_id: int,
        child_msg_id: int,
        chat_id: int,
        user_id: int
    ):
        self.cur.execute(
            '''
            INSERT INTO tasks (
                msg_id,
                child_msg_id,
                chat_id,
                user_id
            )
            VALUES (?, ?, ?, ?);            
            ''',
            (
                msg_id,
                child_msg_id,
                chat_id,
                user_id,
            )
        )
        self.conn.commit()
        logging.info(f'User -- id: {user_id} -- take a task: {msg_id} in channel {chat_id}')
    
    def select_task(
        self,
        child_msg_id: int
    ):
        self.cur.execute(
            '''
            SELECT msg_id, chat_id FROM tasks
            WHERE child_msg_id = (?)
            ''',
            (child_msg_id,)
        )
        return self.cur.fetchone()
