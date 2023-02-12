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

        if usr_inp.split()[0] == "create":
            if usr_inp.split()[1] == "account":
                CLI.create_account(db_conn, users_arr)
            else:
                CLI.unknown()

        elif usr_inp.split()[0] == "login":
            try:
                new_login, flag = CLI.login(
                    db_conn, users_arr, usr_inp.split()[1])

                if flag:
                    instances_arr = DatabaseManip.load_instances_table(db_conn)
                    print("Login Successful.")
                    login_flag = True
                else:
                    print("Wrong credentials.")
            except:
                print("a username must be provided.")

        elif usr_inp.split()[0] == "quit":
            try:
                CLI.quit(db_conn, users_arr, instances_arr)
            except:
                print("leaving without making changes to passwords database")
                exit()

        elif usr_inp.split()[0] == "list":  # list instances
            try:
                CLI.list(new_login, instances_arr)
            except:
                print("to use the database you must be logged to an existing account.\nlogin using 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "add":  # add instance
            try:
                CLI.add(new_login, instances_arr)
            except:
                print("to use the database you must be logged to an existing account.\nlogin using 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "delete":  # remove instance
            try:
                CLI.delete(new_login, instances_arr, usr_inp.split()[1])
            except:
                print("to use the database you must be logged to an existing account.\nlogin using 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "modify":  # modify instance
            try:
                CLI.modify(new_login, instances_arr, usr_inp.split()[1])
            except:
                print("to use the database you must be logged to an existing account.\nlogin using 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "save":  # write instances array to DB and exit
            try:
                CLI.save(db_conn, instances_arr, users_arr)
                break
            except:
                print("to use the database you must be logged to an existing account.\nlogin using 'login' command or 'create account' to create a new account")

        elif usr_inp.split()[0] == "commands":
            CLI.commands()

        elif usr_inp.split()[0] == "user":
            try:
                print(CLI.user(new_login.username))
            except:
                print("not logged in.")

        elif usr_inp.split()[0] == "help":
            CLI.help()

        else:
            CLI.unknown()


if __name__ == "__main__":
    main()
