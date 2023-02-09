import Login
import main
import InstancesHandler
import Instance as it
from random import randint
import Account
import bcrypt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib


def user():
    # print to the terminal the user being used
    pass


def help():
    # supposed to be used along with a <command> as argumentto check how to use it
    pass


def commands():
    # print available commands
    pass


def create_account(connection, users_arr):
    new_id = randint(0, 100)  # think of a better way to define the IDs
    new_username = str(input("username:"))
    new_password = str(input("user's master password:"))
    new_account = Account.Account(connection, users_arr,
                                  new_id,  new_username, new_password)  # creates new Account *object*

    if not new_account.check_existing_credentials(users_arr, new_account.username, new_account.password):
        new_account.add_to_db(connection, users_arr, new_account.id,
                              new_account.username, new_account.password)  # adds to the
        # users_arr the tuple of the account object
        print("Account created. with username:", new_username)
    else:
        print("user already exists")


def login(connection, users_arr):
    usr_username = str(input("username:"))
    print(usr_username, "'s", "master password:")
    usr_password = str(input(""))
    new_login = Login.Login(connection, users_arr,
                            usr_username, usr_password)
    new_login, new_login_flag = new_login.check_correct_credentials(
        users_arr, usr_username, usr_password)

    if not new_login_flag:
        print("wrong credentials.")
        exit()

    print("Login Successful")
    instances_arr = main.load_instances_table(connection)
    return instances_arr, new_login


def quit(connection, users_arr, instances_arr):
    InstancesHandler.InstancesHandler.update_db(
        connection, instances_arr)
    main.terminate_program(connection, users_arr)


def list(new_login, instances_arr):
    InstancesHandler.InstancesHandler.list_instances(
        instances_arr, new_login.id)


def add(new_login, instances_arr):
    # change this random value later to something with an actual pattern
    new_service_id = randint(0, 100)

    new_service_name = str(
        input("type new service name: "))
    new_service_username = str(
        input("type new service username: "))
    new_service_password = str(
        input("type new service password: "))
    new_service_instance = it.Instance(
        new_login.id, new_service_id, new_service_name, new_service_username, new_service_password)

    InstancesHandler.InstancesHandler.add_instance(
        new_service_instance, instances_arr)


def delete(new_login, instances_arr):
    service_id = int(
        input("type the service id:"))
    InstancesHandler.InstancesHandler.remove_instance(
        service_id, instances_arr, new_login.id)


def modify(new_login, instances_arr):
    instance_id = int(input("type the service id:"))
    InstancesHandler.InstancesHandler.modify_instance(
        instance_id, instances_arr, new_login.id)


def save(connection, instances_arr, users_arr):
    InstancesHandler.InstancesHandler.update_db(
        connection, instances_arr)
    main.terminate_program(connection, users_arr)


def unknown():
    print("<unknown command>")


def encrypt_database():
    pass


def decrypt_database():
    pass


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password


def verify_password(password: str, hashed_password: bytes):
    return bcrypt.checkpw(password.encode(), hashed_password)
