import sqlite3
import CLI
import Account
import Login
import Instance as it
import InstancesHandler
from random import randint

# DB related function (move to DB class maybe for better organization)


def start_connection():  # start connection with database
    return sqlite3.connect('pass_mng.db')


def check_tables(db_conn):  # check for users_creds and instances tables
    cur = db_conn.cursor()

    check_users_table = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='users_creds';""").fetchall()  # checking for
    # users credentials table

    if not check_users_table:
        cur.execute(
            "CREATE TABLE users_creds (id integer, username text, password text)")
        db_conn.commit()

    check_instances_table = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' AND name='instances';""").fetchall()  # checking for
    # services instances table

    if not check_instances_table:
        cur.execute(
            "CREATE TABLE instances (owner_id integer, id integer, service_name text, service_username text, "
            "service_password text)")
        db_conn.commit()


def load_users_creds_table(db_conn):
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
    ''' initialization '''
    usr_inp = ""
    db_conn = start_connection()
    check_tables(db_conn)
    users_arr = load_users_creds_table(db_conn)
    print("Welcome to MadPass.\n'quit' to leave.")

    ''' main loop'''
    while usr_inp != "quit":
        usr_inp = str(input(">"))

        if usr_inp == "create account":
            CLI.create_account(db_conn, users_arr)

        elif usr_inp == "login":
            instances_arr, new_login = CLI.login(db_conn, users_arr)

        elif usr_inp == "quit":
            CLI.quit(db_conn, users_arr, instances_arr)

        elif usr_inp == "list":  # list instances
            CLI.list(new_login, instances_arr)

        elif usr_inp == "add":  # add instance
            CLI.add(new_login, instances_arr)

        elif usr_inp == "delete":  # remove instance
            CLI.delete(new_login, instances_arr)

        elif usr_inp == "modify":  # modify instance
            CLI.modify(new_login, instances_arr)

        elif usr_inp == "save":  # write instances array to DB and exit
            CLI.save(db_conn, instances_arr, users_arr)
            break

        else:
            CLI.unknown()


if __name__ == "__main__":
    main()
