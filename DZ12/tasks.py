# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.


import csv
import json
from random import randint

myList = [{'lesson' : 'Химия'},
          {'lesson' : 'Математика'},
          {'lesson' : 'Физика'},
          {'lesson' : 'Русский язык'}]

with open("file.csv", 'w', newline='', encoding='utf-8') as file:
    csv_write = csv.DictWriter(file, fieldnames=[*myList[0]])
    csv_write.writeheader()
    csv_write.writerows(myList)


class descrStr:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not(value.isalpha() and value[0].isupper()):
            raise TypeError("Первая буква должна быть заглавная, в имени должны быть только буквы")
        else:
            setattr(instance, self.name, value)

class Student:
    name = descrStr()
    surname = descrStr()
    patronymic = descrStr()

    def __init__(self, name:str, surname: str, patronymic :str, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._myList = self.grades()
        self.performance = self.setGrades()
        self.jsonExport()

    def grades(self):
        with open("file.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            myList = []
            for row in reader:
                myList.append(row["lesson"])
        return myList

    def setGrades(self):
        gradeDict = {}
        for i in self._myList:
            x = randint(2, 5)
            y = randint(2, 5)
            z = randint(2, 5)
            iTest = randint(20, 100)
            gradeDict[i] = f"{x}, {y}, {z}    средний балл - {round((x+y+z)/3, 2)},    Итоговое тестирование - {iTest}"
        return gradeDict

    def printSt(self):
        print("#"*100)
        print(f'{self.surname} {self.name[0]}. {self.patronymic[0]} ')
        print(" "+';\n '.join([f'{key.capitalize()}: {value}' for key, value in self.performance.items()]))

    def jsonExport(self):
        with open("students.json", 'a', encoding='utf-8') as json_f:
            json.dump(self.__dict__, json_f, indent=4, ensure_ascii=False)

ob = Student("Татьяна", "Иванова", "Петровна")
ob2 = Student("Александр", "Петров", "Сергеевич")
ob3 = Student("Никита", "Сидоров", "Иванович")

ob.printSt()
ob2.printSt()
ob3.printSt()