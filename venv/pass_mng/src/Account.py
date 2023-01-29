import sqlite3


class Account:
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password

    def check_new_credentials(username, password):
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_db_cursor.execute(
            "SELECT username, password FROM users WHERE username = ? and password = ?" (username, password))

    def add_to_db(id, username, password):
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_db_cursor.execute(
            "INSERT INTO users VALUES(?, ?, ?)", (id, username, password))
        users_conn.commit()
        users_conn.close()
