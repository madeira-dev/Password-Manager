import sqlite3
from Account import *
from Login import *
from InstancesHandler import *
from random import *


def start_connection():  # start connection with database
    db_conn = sqlite3.connect('pass_mng.db')
    users_db_cursor = db_conn.cursor()
    users_db_cursor.execute("SELECT * FROM users_creds;")
    rows = users_db_cursor.fetchall()

    # loading all rows into an array for faster queries
    users_arr = []
    for row in rows:
        users_arr.append(row)

    return db_conn, users_arr


######################################
# probably change these global variable later #
db_conn, users_arr = start_connection()
######################################


def check_tables():  # function to check if the table exists in the database
    conn_cur = user_db_conn.cursor()

    check_users_table = conn_cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='users_creds';""").fetchall()  # checking for users credentials table

    if check_users_table == []:
        conn_cur.execute(
            "CREATE TABLE users_creds (id integer, username text, password text)")
        user_db_conn.commit()

    check_instances_table = conn_cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='instances';""").fetchall()  # checking for services instances table

    if check_instances_table == []:
        conn_cur.execute(
            "CREATE TABLE instances (id integer, service_name text, service_username text, service_password text)")
        user_db_conn.commit()


def terminate_program():
    conn_cur = user_db_conn.cursor()
    conn_cur.execute("DELETE FROM users_creds;")
    user_db_conn.commit()

    for user in users_arr:
        conn_cur.execute(
            "INSERT INTO users_creds VALUES (?, ?, ?);", (user[0], user[1], user[2]))
        user_db_conn.commit()
    user_db_conn.close()

    return


def load_instances_table():
    instances_db_cursor = db_conn.cursor()
    instances_db_cursor.execute("SELECT * FROM instances;")
    rows = instances_db_cursor.fetchall()

    instances_arr = []
    for row in rows:
        instances_arr.append(row)

    return instances_arr


def main():
    usr_inp = -1
    instances_input = -1
    check_tables()

    while usr_inp != 0:
        print("""Choose the option:
        1. Create Account
        2. Login
        0. Exit""")

        usr_inp = int(input("type the option number: "))

        if usr_inp == 0:
            terminate_program()

        if usr_inp == 1:  # new account
            new_id = randint(0, 100)  # think of a better way to define the IDs
            new_username = str(input("type the new username: "))
            new_password = str(input("type the new password: "))
            new_account = Account(user_db_conn, users_arr,
                                  new_id,  new_username, new_password)  # creates new Account *object*

            if not new_account.check_existing_credentials(users_arr, new_account.username, new_account.password):
                new_account.add_to_db(
                    user_db_conn, users_arr, new_account.id, new_account.username, new_account.password)  # adds to the users_arr the tuple of the account object
            else:
                print("user already exists")

        elif usr_inp == 2:  # login to existing account
            usr_username = str(input("type the username: "))
            usr_password = str(input("type the password: "))
            new_login = Login(user_db_conn, users_arr,
                              usr_username, usr_password)

            if not (new_login.check_correct_credentials(users_arr, new_login.username, new_login.password)):
                print("wrong credentials.")
                return
            print("Login Successful")

            while instances_input != 5:
                print("""
Choose the option:
        1. List services accounts
        2. Add new service account
        3. Remove service account
        4. Modify service account
        5. Exit""")

                instances_input = int(input("type the option number: "))

                if instances_input == 1:
                    InstancesHandler.list_instances()

                elif instances_input == 2:
                    new_service_id = int(
                        input("type the new service id: "))
                    new_service_name = str(
                        input("type new service name: "))
                    new_service_username = str(
                        input("type new service username: "))
                    new_service_password = str(
                        input("type new service password: "))

                    InstancesHandler.add_instance(
                        new_service_id, new_service_name, new_service_username, new_service_password)

                elif instances_input == 3:
                    service_id = int(
                        input("type the id of the service you want to remove: "))

                    InstancesHandler.remove_instance(service_id)

                elif instances_input == 4:
                    InstancesHandler.modify_instance()

                elif instances_input == 5:
                    break


if __name__ == "__main__":
    main()
