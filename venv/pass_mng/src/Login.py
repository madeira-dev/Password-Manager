import Account


class Login:
    def __init__(self, connection, users_arr, username, password) -> None:
        self.connection = connection
        self.users_arr = users_arr
        self.username = username
        self.password = password

    def check_correct_credentials(self, users_arr, username, password):
        flag = False
        found_id = 0
        found_username = ""
        found_password = ""
        for account in users_arr:
            if account[1] == username and account[2] == password:
                flag = True
                found_id = account[0]
                found_username = account[1]
                found_username = account[2]

        return Account.Account(
            self.connection, users_arr, found_id, found_username, found_password), flag
