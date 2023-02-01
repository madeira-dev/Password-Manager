import sqlite3
from CLI import *


class Login:
    def __init__(self, users_arr, id, username, password) -> None:
        self.id = id
        self.users_arr = users_arr
        self.username = username
        self.password = password

    def check_existing_credentials(self, users_arr, username):
        conn, users_array = self.start_connection()
        flag = False

        for account in users_array:
            if account[1] == username:
                flag = True

        conn.close()

        return flag

    def check_correct_credentials(self, users_arr, username, password):
        conn, users_arr = self.start_connection()
        main_flag = False

        for account in users_arr:
            if account[1] == username and account[2] == password:
                main_flag = True

        conn.close()

        return main_flag
