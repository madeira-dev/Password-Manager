import sqlite3
from CLI import *


class Account:
    def __init__(self, users_arr, id, username, password) -> None:
        self.id = id
        self.users_arr = users_arr
        self.username = username
        self.password = password

    def check_new_credentials(self, users_arr, username, password):
        users_conn = sqlite3.connect('pass_mng.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_db_cursor.execute(
            "SELECT username, password FROM users WHERE username = ? and password = ?", (username, password))
        users_conn.close()

    def add_to_db(self, users_arr, id, username, password):
        users_conn = sqlite3.connect('pass_mng.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_db_cursor.execute(
            "INSERT INTO users_creds VALUES(?, ?, ?)", (id, username, password))
        users_conn.commit()
        users_conn.close()
