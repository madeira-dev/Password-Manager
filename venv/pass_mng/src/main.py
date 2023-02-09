import sqlite3
import CLI
import DatabaseManip


def main():
    ''' initialization '''
    usr_inp = ""
    db_conn = DatabaseManip.start_connection()
    DatabaseManip.check_tables(db_conn)
    users_arr = DatabaseManip.load_users_creds_table(db_conn)
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
