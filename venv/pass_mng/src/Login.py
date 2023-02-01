import sqlite3


class Login:
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password

    def start_connection(self):
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()
        users_db_cursor.execute("SELECT * FROM users_creds")
        rows = users_db_cursor.fetchall()

        # loading all rows into an array for faster queries
        users_arr = []
        for row in rows:
            users_arr.append(row)

        return users_conn, users_arr

    def check_existing_credentials(self, username):
        conn, users_array = self.start_connection()
        flag = False

        for account in users_array:
            if account[1] == username:
                flag = True

        conn.close()

        return flag

    def check_correct_credentials(self, username, password):
        conn, users_arr = self.start_connection()
        main_flag = False

        for account in users_arr:
            if account[1] == username and account[2] == password:
                main_flag = True

        conn.close()

        return main_flag
