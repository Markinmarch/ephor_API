import logging


from telegram_bot.sql_db.bot_tables import Bot_tables_DB


class Posts(Bot_tables_DB):

    def insert_post(
        self,
        post_id: int,
        user_id: int
    ):
        self.cur.execute(
            '''
            INSERT INTO posts (
                id,
                user_id
            )
            VALUES (?, ?);            
            ''',
            (
                post_id,
                user_id,
            )
        )
        self.conn.commit()
        logging.info(f'User -- id: {user_id} -- created a post: {post_id}')

    def select_user(
        self,
        post_id: int
    ):
        self.cur.execute(
            '''
            SELECT user_id FROM posts
            WHERE id = (?)
            ''',
            (post_id,)
        )
        return self.cur.fetchone()
    
    def select_posts(
        self,
        user_id: int
    ):
        self.cur.execute(
            '''
            SELECT id FROM posts
            WHERE user_id = (?)
            ''',
            (user_id,)
        )
        return self.cur.fetchall()
    
    def select_all_data(self):
        self.cur.execute(
            '''
            SELECT * FROM posts
            '''
        )
        return self.cur.fetchall()
    
    def delete_post(
        self,
        post_id: int
    ):
        self.cur.execute(
            '''
            DELETE FROM posts
            WHERE id = (?)
            ''',
            (post_id,)
        )
        self.conn.commit()
        logging.info(f'Posts {post_id} has been deleted')
    
    def check_quantity_posts(
            self,
            user_id: int
    ):
        self.cur.execute(
            '''
            SELECT COUNT(id) FROM posts
            WHERE user_id = (?)
            ''',
            (user_id,)
        )
        return self.cur.fetchone()[0]

    def delete_posts_table(self) -> None:
        self.cur.execute(
            '''
            DELETE FROM posts;
            '''
        )
        self.conn.commit()

posts = Posts()