'''
Задача:
Написать генератор, который принимает путь к файлу.
При каждой итерации возвращает md5 хеш каждой строки файла.
'''

import hashlib


def hash_line(path):
    m = hashlib.md5()

    with open(path, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            m.update(line.encode('utf-8'))
            yield m.hexdigest()


generator = hash_line('input_file.txt')

for item in generator:
    print(item)
