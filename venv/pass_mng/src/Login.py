import sqlite3
from CLI import *


class Login:
    def __init__(self, connection, users_arr, username, password) -> None:
        self.connection = connection
        self.users_arr = users_arr
        self.username = username
        self.password = password

    def check_existing_credentials(self, connection, users_arr, username, password):
        flag = False

        for account in users_arr:
            if account[1] == username and account[2] == password:
                flag = True

        return flag

    def check_correct_credentials(self, connection, users_arr, username, password):
        main_flag = False

        for account in users_arr:
            if account[1] == username and account[2] == password:
                main_flag = True

        return main_flag

    def add_to_db(self, connection, users_arr, id, username, password):
        new_account = Login(connection, users_arr, id, username, password)
        users_arr.append(new_account)
