import CLI
import DatabaseManip


def main():
    ''' initialization '''
    usr_inp = ""
    db_conn = DatabaseManip.start_connection()
    DatabaseManip.check_tables(db_conn)
    users_arr = DatabaseManip.load_users_creds_table(db_conn)
    login_flag = False
    print("Welcome to MadPass.\n'quit' to leave.")

    ''' main loop'''
    while usr_inp != "quit":
        usr_inp = str(input(">"))

        if usr_inp.split()[0] == "create account":
            CLI.create_account(db_conn, users_arr)

        elif usr_inp.split()[0] == "login":
            instances_arr, new_login = CLI.login(
                db_conn, users_arr, usr_inp.split()[1])
            login_flag = True

        elif usr_inp.split()[0] == "quit":
            if login_flag:
                print("Goodbye!!")
                CLI.quit(db_conn, users_arr, instances_arr)
            else:
                print("Goodbye!!")
                exit()

        elif usr_inp.split()[0] == "list":  # list instances
            if login_flag:
                CLI.list(new_login, instances_arr)
            else:
                print("to use the database you must be logged to an existing account.\nto login use 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "add":  # add instance
            if login_flag:
                CLI.add(new_login, instances_arr)
            else:
                print("to use the database you must be logged to an existing account.\nto login use 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "delete":  # remove instance
            if login_flag:
                CLI.delete(new_login, instances_arr, usr_inp.split()[1])
            else:
                print("to use the database you must be logged to an existing account.\nto login use 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "modify":  # modify instance
            if login_flag:
                CLI.modify(new_login, instances_arr, usr_inp.split()[1])
            else:
                print("to use the database you must be logged to an existing account.\nto login use 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "save":  # write instances array to DB and exit
            if login_flag:
                CLI.save(db_conn, instances_arr, users_arr)
                break
            else:
                print("to use the database you must be logged to an existing account.\nto login use 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "commands":
            CLI.commands()

        elif usr_inp.split()[0] == "user":
            if login_flag:
                CLI.user(new_login.username)
            else:
                print("not logged in.")

        elif usr_inp.split()[0] == "help":
            CLI.help()

        else:
            CLI.unknown()


if __name__ == "__main__":
    main()
