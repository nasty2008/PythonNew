

   # Вспоминаем задачу 3 из прошлого семинара: 
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.

#  Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. 
#  Имена пишите с большой буквы. 
#  Каждую пару сохраняйте с новой строки.

import json


def toJson():
    myDict = {}
    with open(f"c:\\Users\\User\\Desktop\\Seminar8\\Untitled-1.txt", "r", encoding="utf-8") as nf :
        while res := nf.readline():
            myList = res.replace("\n", "").upper().split(' | ')
            myDict[myList[0]] = myList[1]
        nn.close()
    print(myDict)
    with open(f"c:\\Users\\User\\Desktop\\Seminar8\\new_user.json", 'w', encoding="utf-8") as f:
        result = json.dumps(myDict, indent=2, separators=(',', ':'), sort_keys=True)
        f.write(result)
        f.close()

toJson()



# Напишите функцию, которая в бесконечном цикле:
#       - запрашивает имя, 
#       - личный идентификатор 
#       - уровень доступа (от 1 до 7). 
#  📌 После каждого ввода добавляйте новую информацию в JSON файл. 
#  📌 Пользователи группируются по уровню доступа.
#  📌 Идентификатор пользователя выступает ключём для имени. 
#  📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
#  📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

import json


def getAccessLevel():
    accessLevels = ['1', '2', '3', '4', '5', '6', '7']

    with open('access_file.json', 'r', encoding='utf-8') as read_access:
        myDict = json.load(read_access)                             # прочитать данные из файла
        print(myDict)
        read_access.close()

        while True:                                                                    # запусить бесконечный цикл: пока словарь есть...
            ident = input("введите личный идентификатор: ")
            if ident in myDict.keys() :                                        # если есть идентиф-р в ключах словаря, написать сообщение
                print("идентификатор уже используется")
            else :
                while True:
                    access = input(f"введите уровень доступа с {min(accessLevels)} по {max(accessLevels)} : ")
                    if access not in accessLevels :
                        print ("некорректный ввод")
                    else :
                        myDict[ident] = access
                        sortedDict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse=True))  # если reverse=True, то элементы числового списка отсорт по убыванию 
                        print(sortedDict)

                        with open('access_file.json', 'w', encoding="utf-8") as write_access:
                            new_entry = json.dumps(sortedDict, indent=2, separators=(',', ':'))
                            write_access.write(new_entry)
                            write_access.close()
                            break
                break

getAccessLevel()




#  Напишите функцию, которая 
#    📌 ищет json файлы в указанной директории
#    📌 сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle

def search_jsonfiles():
    file = 'new_user.json'
    with open(f'c:\\Users\\User\\Desktop\\Seminar8\\new_user.json', 'r', encoding='utf-8') as readers_dir:
        list_direct = json.load(readers_dir)
        readers_dir.close()

    with open(f'c:\\Users\\User\\Desktop\\Seminar8\\new_user.pickle', 'wb') as writes:
        writ_namefile = pickle.dump(writ_namefile, writes)        # в аргументы передать объект и файл
        writes.close()

search_jsonfiles()


#  Напишите функцию, которая преобразует pickle файл, 
#  хранящий список словарей в табличный csv файл. 
### 📌 Для тестирования возьмите pickle версию файла из задачи 4 этого семинара. 
###📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle
from pathlib import Path


def pickle2csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write,
    ):
        data = pickle.load(f_read)
        
        keys = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    pickle2csv(Path('new_users.pickle'))