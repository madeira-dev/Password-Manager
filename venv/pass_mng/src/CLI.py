import Login
import InstancesHandler
import Instance as it
import Account
import DatabaseManip
import bcrypt
import getpass
import hashlib
from random import randint
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def user(username):
    return username


def help():
    print("to use help, type help <command> to understand how to use the <command>")


def commands():
    print("list  add  delete  modify  save")
    print("type 'help <command>' and check how to use it")


def create_account(connection, users_arr):
    new_id = randint(0, 100)  # think of a better way to define the IDs
    new_username = str(input("username:"))
    new_password = str(getpass.getpass(new_username + "'s master password:"))
    new_account = Account.Account(connection, users_arr,
                                  new_id,  new_username, new_password)  # creates new Account *object*

    if not new_account.check_existing_credentials(users_arr, new_account.username, new_account.password):
        new_account.add_to_db(connection, users_arr, new_account.id,
                              new_account.username, new_account.password)  # adds to the

        # users_arr the tuple of the account object
        print("Account created with username:", new_username)
    else:
        print("user already exists")


def login(connection, users_arr, usr_username):
    usr_password = str(getpass.getpass(usr_username + "'s master password:"))

    new_login = Login.Login(connection, users_arr,
                            usr_username, usr_password)

    tmp, new_login_flag = new_login.check_correct_credentials(
        users_arr, usr_username, usr_password)

    return new_login, new_login_flag


def quit(connection, users_arr, instances_arr):
    InstancesHandler.InstancesHandler.update_db(
        connection, instances_arr)

    DatabaseManip.terminate_program(connection, users_arr)


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


def delete(new_login, instances_arr, service_id):
    InstancesHandler.InstancesHandler.remove_instance(
        service_id, instances_arr, new_login.id)


def modify(new_login, instances_arr, instance_id):
    InstancesHandler.InstancesHandler.modify_instance(
        instance_id, instances_arr, new_login.id)


def save(connection, instances_arr, users_arr):
    InstancesHandler.InstancesHandler.update_db(
        connection, instances_arr)

    DatabaseManip.terminate_program(connection, users_arr)


def unknown():
    print("unknown command. Maybe use 'commands' and check the avaiable commands.")


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
