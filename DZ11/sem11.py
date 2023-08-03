# Задача 1

# Создайте класс 'Моя Строка', где:
# будут доступны все возможности str,
# дополнительно хранятся имя автора строки и время создания (time.time).

import time
class MyString(str):

    def __new__(cls, text, nameAuthor):
        instance = super().__new__(cls, text)
        instance.t = time.time()
        instance.author = nameAuthor
        return instance

text = """Author comment"""
d = MyString(text, "Alex")
print(d.__dict__)

# Задача 2

# Создайте класс 'Архив', который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов,
# list-архивы также являются свойствами экземпляра.

class Archive():
    _flag = None
    """Почему комментарии в самом классе? Потому что это документация ©Зухра"""


    def __new__(cls, number, text):
        """"Непонятная функция заполняет архив старыми значениями"""

        if cls._flag == None:
            cls._flag = super().__new__(cls)
            cls._flag.archNumber = []
            cls._flag.archText = []
        elif cls._flag != None:
            cls._flag.archText.append(cls._flag.text)
            cls._flag.archNumber.append(cls._flag.number)
        return cls._flag

    def __init__(self, number, text):
        self.number = number
        self.text = text

    def __str__(self):
        return f'{"".join(x for x in self.archText)} - архив,  текущий номер {self.number}'

    def __repr__(self):
        return f'{self.text}'

    def docs(self):
        return self.__doc__

t = Archive(12, "jksagdjsagdkjalhsdk aksjdhlka jahdk kjahs")
t2 = Archive(12, "jksagdjsagdkjalhsdk sadqqqqq qqqq")
print()
print(t2)
print(repr(t2))

# Задача 3

# Добавьте к задачам 1 и 2 строки документации для классов.

# Задача 4

# Доработаем класс 'Архив' из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

# Задача 5

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        c = self.a + other.a
        d = self.b + other.b
        return rectangle(c, d)

    def __sub__(self, other):
        p1 = 2 * (self.a+self.b)
        p2 = 2 * (other.a + other.b)
        if p1 > p2 :
            c = self.a - other.a
            d = self.b - other.b
        else:
            c = other.a - self.a
            d = other.b - self.b
        return rectangle(c,d)

    def __str__(self):
        return "x".join([str(self.a), str(self.b)])

    def __eq__(self, other):
        if self.a * self.b == other.a * other.b:
            return True
        else : return False

    def __lt__(self, other):
        if self.a * self.b < other.a * other.b:
            return True
        else: return False

    def __le__(self, other):
        if self.a * self.b > other.a * other.b: return True
        else : False


pr1 = rectangle(2, 4)
pr2 = rectangle(4, 2)
print(pr1-pr2, pr1+pr2)
print(pr1==pr2)
print(pr1<pr2)

# Задача 6

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения.
