class Account:
    def __init__(self, id, username, acc_password) -> None:
        self.id = id
        self.username = username
        self.acc_password = acc_password

    # create method to send new account to SQLite database
    # def add_to_db():
