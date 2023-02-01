import sqlite3
from Account import *
from Login import *
from InstancesHandler import *
from random import *


def check_tables():  # function to check if the table exists in the database
    conn = sqlite3.connect('pass_mng.db')  # main database
    conn_cur = conn.cursor()

    check_users_table = conn_cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='users_creds';""").fetchall()  # checking for users credentials table

    if check_users_table == []:
        conn_cur.execute(
            "CREATE TABLE users_creds (id integer, username text, password text)")
        conn.commit()
    else:
        pass

    check_instances_table = conn_cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='instances';""").fetchall()  # checking for services instances table

    if check_instances_table == []:
        conn_cur.execute(
            "CREATE TABLE instances (id integer, service_name text, service_username text, service_password text)")
        conn.commit()
    else:
        pass

        conn.close()


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

        if usr_inp == 1:
            new_id = randint(0, 100)  # think of a better way to define the IDs
            new_username = str(input("type the new username: "))
            new_password = str(input("type the new password: "))
            new_account = Account(new_id, new_username, new_password)
            res = Login(new_id, new_username, new_password)

            if res.check_existing_credentials(new_account.username):
                print("user already exists")
            else:
                Account.add_to_db(
                    new_account.id, new_account.username, new_account.password)

        elif usr_inp == 2:
            usr_id = 0
            usr_username = str(input("enter your username: "))
            usr_password = str(input("enter the password: "))
            new_login = Login(usr_id, usr_username, usr_password)

            if not(new_login.check_correct_credentials(
                    new_account.username, new_account.password)):
                print("wrong credentials.")
                return

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
