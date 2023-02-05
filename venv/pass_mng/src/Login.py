from main import *


class Login:
    def __init__(self, connection, users_arr, username, password) -> None:
        self.connection = connection
        self.users_arr = users_arr
        self.username = username
        self.password = password

    def check_correct_credentials(self, users_arr, username, password):
        flag = False
        for account in users_arr:
            if account[1] == username and account[2] == password:
                flag = True
        return account[0], flag
