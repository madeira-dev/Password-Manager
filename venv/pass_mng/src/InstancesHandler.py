import Instance as it
import sqlite3


class InstancesHandler():
    def __init__(self, **kwargs) -> None:
        instances_arr = kwargs.get("instances_arr", None)
        pass

    def list_instances():
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_db_cursor.execute("SELECT * FROM users")
        rows = users_db_cursor.fetchall()

        for row in row:
            print(row)

        users_conn.close()

    def add_instance(service_id, service_name, service_username, service_password):
        new_instance = it.Instance(
            service_id, service_name, service_username, service_password)
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_db_cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?)",
                                (service_id, service_name, service_username, service_password))
        users_conn.close()

    def remove_instance(id):
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_conn.close()

    def modify_instance(username, password):
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_conn.close()

    def search_instance(username, password):
        users_conn = sqlite3.connect('users.db')
        users_db_cursor = users_conn.cursor()  # cursor to interact with users database

        users_conn.close()
