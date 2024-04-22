# AuthenticationModule:
#     def __init__(self, user_database):
#         self.user_database = user_database
#
#     def authenticate(self, username, password):
#         if username in self.user_database:
#             if self.user_database[username] == password:
#                 return True
#
#
#
# if __name__ == "__main__":
#
#     user_database = {
#         "user1": "password1",
#         "user2": "password2",
#
#     }
#
#
#     auth_module = AuthenticationModule(user_database)
#
#     # Пример аутентификации
#     username = input("Введите имя пользователя: ")
#     password = input("Введите пароль: ")
#
#     if auth_module.authenticate(username, password):
#         print("Аутентификация прошла успешно!")
#     else:
#         print("Неверное имя пользователя или пароль!")
