import logging


from telegram_bot.sql_db.bot_tables import Bot_tables_DB

class Responders(Bot_tables_DB):

    def respond_post(
        self,
        responder_id: int,
        post_id: int
    ):
        self.cur.execute(
            '''
            INSERT INTO responders (
                responder_id,
                post_id
            )
            VALUES (?, ?);            
            ''',
            (
                responder_id,
                post_id
            )
        )
        self.conn.commit()
        logging.info(f'User -- id: {responder_id} -- respond a post: {post_id}')

    def checking_responses(
        self,
        responder_id: int,
        post_id: int
    ):
        self.cur.execute(
            '''
            SELECT COUNT(*) FROM responders
            WHERE responder_id = ? AND post_id = ?
            ''',
            (
                responder_id,
                post_id
            )
        )
        return self.cur.fetchone()[0]
    
    def delete_responders_table(self) -> None:
        self.cur.execute(
            '''
            DELETE FROM responders;
            '''
        )
        self.conn.commit()

responders = Responders()
