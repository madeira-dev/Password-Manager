import Account as acc
import Login as lg


def main():
    usr_inp = -1
    while usr_inp != 0:
        print("""Choose the option:
        1. Create Account
        2. Login
        0. Exit""")

        usr_inp = int(input("type the number: "))

        if usr_inp == 1:
            print("-create account selected-")
            new_id = 0  # tmp value. change to hashed value later
            # call hashing funtcion
            new_username = str(input("type the new username: "))
            new_password = str(input("type the new password: "))
            acc.Account(new_id, new_username, new_password)

        elif usr_inp == 2:
            print("-login selected-")
            usr_id = 0
            usr_username = str(input("enter your username: "))
            usr_password = str(input("enter the password: "))
            lg.Login(usr_id, usr_username, usr_password)


if __name__ == "__main__":
    main()
