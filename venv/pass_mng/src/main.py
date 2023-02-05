import sqlite3
from CLI import *
from Account import *
from Login import *
from Instance import *
from InstancesHandler import *
from random import *

# DB related function (move to DB class maybe for better organization)


def start_connection():  # start connection with database
    return sqlite3.connect('pass_mng.db')


def check_tables(db_conn):  # check for users_creds and instances tables
    cur = db_conn.cursor()

    check_users_table = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='users_creds';""").fetchall()  # checking for users credentials table

    if check_users_table == []:
        cur.execute(
            "CREATE TABLE users_creds (id integer, username text, password text)")
        db_conn.commit()

    check_instances_table = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='instances';""").fetchall()  # checking for services instances table

    if check_instances_table == []:
        cur.execute(
            "CREATE TABLE instances (owner_id integer, id integer, service_name text, service_username text, service_password text)")
        db_conn.commit()


def load_users_creds(db_conn):
    users_db_cursor = db_conn.cursor()
    users_db_cursor.execute("SELECT * FROM users_creds;")
    rows = users_db_cursor.fetchall()

    users_arr = []
    for row in rows:
        users_arr.append(row)

    return users_arr


def load_instances_table(db_conn):
    instances_db_cursor = db_conn.cursor()
    instances_db_cursor.execute("SELECT * FROM instances;")
    rows = instances_db_cursor.fetchall()

    instances_arr = []
    for row in rows:
        instances_arr.append(row)

    return instances_arr


def terminate_program(db_conn, users_arr):
    conn_cur = db_conn.cursor()
    conn_cur.execute("DELETE FROM users_creds;")
    db_conn.commit()

    for user in users_arr:
        conn_cur.execute(
            "INSERT INTO users_creds VALUES (?, ?, ?);", (user[0], user[1], user[2]))
        db_conn.commit()
    db_conn.close()

    return


def main():
    usr_inp = -1
    instances_input = -1
    db_conn = start_connection()
    check_tables(db_conn)
    users_arr = load_users_creds(db_conn)

    while usr_inp != 0:
        print("""Choose the option:
        1. Create Account
        2. Login
        0. Exit""")

        usr_inp = int(input("type the option number: "))

        if usr_inp == 0:
            terminate_program(db_conn, users_arr)

        if usr_inp == 1:  # new account
            new_id = randint(0, 100)  # think of a better way to define the IDs
            new_username = str(input("type the new username: "))
            new_password = str(input("type the new password: "))
            new_account = Account(db_conn, users_arr,
                                  new_id,  new_username, new_password)  # creates new Account *object*

            if not new_account.check_existing_credentials(users_arr, new_account.username, new_account.password):
                new_account.add_to_db(
                    db_conn, users_arr, new_account.id, new_account.username, new_account.password)  # adds to the users_arr the tuple of the account object
            else:
                print("user already exists")

        elif usr_inp == 2:  # log in to existing account
            usr_username = str(input("type the username: "))
            usr_password = str(input("type the password: "))
            new_login = Login(db_conn, users_arr,
                              usr_username, usr_password)
            new_login_id, new_login_flag = new_login.check_correct_credentials(
                users_arr, usr_username, usr_password)

            if not (new_login_flag):
                print("wrong credentials.")
                return
            print("Login Successful")
            instances_arr = load_instances_table(db_conn)

            while instances_input != 5:
                print("""
Choose the option:
        1. List services accounts
        2. Add new service account
        3. Remove service account
        4. Modify service account
        5. Exit""")

                instances_input = int(input("type the option number: "))

                if instances_input == 1:  # list instances
                    InstancesHandler.list_instances(
                        instances_arr, new_login_id)

                elif instances_input == 2:  # add instance
                    # change this random value later to something with an actual pattern
                    new_service_id = randint(0, 100)

                    new_service_name = str(
                        input("type new service name: "))
                    new_service_username = str(
                        input("type new service username: "))
                    new_service_password = str(
                        input("type new service password: "))
                    new_service_instance = Instance(
                        new_login_id, new_service_id, new_service_name, new_service_username, new_service_password)

                    InstancesHandler.add_instance(
                        new_service_instance, instances_arr)

                elif instances_input == 3:  # remove instance
                    service_id = int(
                        input("type the id of the service you want to remove: "))

                    InstancesHandler.remove_instance(
                        service_id, instances_arr, new_login_id)

                elif instances_input == 4:  # modify instance
                    instance_to_modify = str(
                        input("type the service name to change the informations: "))
                    InstancesHandler.modify_instance(
                        instance_to_modify, instances_arr, new_login_id)

                elif instances_input == 5:  # write instances array to DB and exit
                    InstancesHandler.update_db(db_conn, instances_arr)
                    break


if __name__ == "__main__":
    main()
