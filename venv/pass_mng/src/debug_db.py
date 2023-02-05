import sqlite3
users_conn = sqlite3.connect('pass_mng.db')
users_db_cursor = users_conn.cursor()

users_db_cursor.execute("DROP TABLE instances;")
# # data
# test0 = 1
# test1 = "madeira"
# test2 = "password"
# # add to db
# users_db_cursor.execute(
#     "INSERT INTO users_creds VALUES(?, ?, ?);", (test0, test1, test2))
# users_conn.commit()
# # load into array
# users_db_cursor.execute("SELECT * FROM users_creds;")
# rows = users_db_cursor.fetchall()
# users_arr = []
# for row in rows:
#     users_arr.append(row)
# # debug print
# # print(users_arr)
# # deleting from db
# # users_db_cursor.execute("DELETE FROM users_creds;")
# # users_conn.commit()
# # # transfer from array to db
# # for user in users_arr:
# #     users_db_cursor.execute("INSERT INTO users_creds VALUES (?, ?, ?);", user)
# #     users_conn.commit()
# users_conn.close()


# class Account:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password


# accounts = [Account(1, "user1", "pass1"), Account(
#     2, "user2", "pass2"), Account(3, "user3", "pass3")]

# accounts_list = [(account.id, account.username, account.password)
#                  for account in accounts]

# print(accounts_list)
