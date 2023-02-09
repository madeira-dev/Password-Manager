import sqlite3


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
