# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть
# уникальный идентификатор (ID),
# имя и
# уровень доступа.
# Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._level = 'user'
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_level(self, level):
        self._level = level

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._level = 'admin'
        self._user_list = [] # у каждого админа получится свой список пользваотелей,
                             # в идеале список пользователей должен быть не в этом классе,
                            # но пока непонятно как это сделать.

    def add_user(self, new_user):
        self._user_list.append(new_user)
        print(f"Пользователь {new_user.get_name()} добавлен в список")

    def remote_user(self, del_user):
        # удаление пользователя
        if del_user in self._user_list:
            self._user_list.remove(del_user)
            print(f"Пользователь {del_user.get_name()} удален")
        else:
            print(f"Пользователь {del_user.get_name()} не найден")

    def print_list_users(self):
        print("Список пользователей")
        for user in self._user_list:
            print(f"{user.get_id()} - {user.get_name()} - {user.get_level()}")


user01 = User(12345, "Иванов Иван Иванович")
user02 = User(12346, "Петров Василий Иванович")
user03 = User(12347, "Сидоров Иван Петрович")
user04 = User(12348, "Кузнецов Андрей Александрович")
user05 = User(12349, "Козлов Роман Юрьевич")

admin01 = Admin(12340, "Шубин Игорь Петрович")
admin02 = Admin(12341, "Васин Кирилл Сергеевич")

admin01.add_user(user01)
admin01.add_user(user02)
admin01.add_user(user03)
admin01.add_user(user04)
admin01.add_user(admin01)

admin01.print_list_users()

# проверяем защищенность атрибутов
print(f"user01.name = {user01._name} - 'name' дает ошибку, '_name' - не рекомендуется использовать")
print(f"user01.name = {user01.get_name()}")
print(f"user01.id = {user01.get_id()}")
print(f"user01.level = {user01.get_level()}")