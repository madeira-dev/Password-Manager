from Account import *
from Login import *
from InstancesHandler import *


def main():
    usr_inp = -1
    instances_input = -1

    while usr_inp != 0:
        print("""Choose the option:
        1. Create Account
        2. Login
        0. Exit""")

        usr_inp = int(input("type the option number: "))

        if usr_inp == 1:
            print("-create account selected-")
            new_id = 0  # tmp value. change to random value later
            # call randomizing function
            new_username = str(input("type the new username: "))
            new_password = str(input("type the new password: "))
            Account(new_id, new_username, new_password)
            # verify if user is new, if it is, get back to this screen so user can login

        elif usr_inp == 2:
            print("-login selected-")
            usr_id = 0
            usr_username = str(input("enter your username: "))
            usr_password = str(input("enter the password: "))
            Login(usr_id, usr_username, usr_password)
            # if successful login, call new menu with instances options

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
