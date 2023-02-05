class Account:
    def __init__(self, connection, users_arr, id, username, password) -> None:
        self.connection = connection
        self.users_arr = users_arr
        self.id = id
        self.username = username
        self.password = password

    def check_existing_credentials(self, users_arr, username, password):
        flag = False
        for account in users_arr:
            if account[1] == username and account[2] == password:
                flag = True
        return flag

    def add_to_db(self, connection, users_arr, id, username, password):
        new_account = Account(connection, users_arr, id, username, password)
        new_account_tuple = (
            new_account.id, new_account.username, new_account.password)
        users_arr.append(new_account_tuple)
