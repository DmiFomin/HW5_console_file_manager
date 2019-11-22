import os
import shutil
import sys


def get_program_info():
    """
    Информация о программе
    """
    return {'OS': f'{sys.platform}, ({os.name})', 'author': 'Fomin Dmitry'}


def get_program_settings():
    """
    Получаем настройки программы
    :return: Возвращаем словарь с настройками
    """
    program_settings = {'path_to_listdir': os.path.join(os.getcwd(), 'listdir.txt')}
    return program_settings


def create_folder():
    """
    Создание каталога
    """
    folder_name = input('Введите название каталога: ')
    # Проверяем есть каталог или нет
    if os.path.exists(folder_name):
        print('Каталог уже существует!')
    else:
        os.mkdir(folder_name)
        print('Создан каталог: ', os.path.join(os.getcwd(), folder_name))


def delete_folder():
    """
    Удаление каталога или файла
    """
    folder_name = input('Введите название каталога или файла: ')
    path = os.path.join(os.getcwd(), folder_name)
    # Проверяем есть каталог или нет
    if os.path.exists(path):
        # Проверяем каталог это или файл
        if os.path.isdir(path):
            # Если каталог, то проверяем содержит ли он подкаталоги или файлы
            if len(os.listdir(path)) > 0:
                answer = input('Каталог не пустой! Удалить его и все его содержимое (Да/Нет)? ')
                # Специально прописал условие только на один ответ "Да", чтобы только при нем каталог удалился
                if answer == 'Да':
                    shutil.rmtree(path)
                return
        os.rmdir(path)
    else:
        print('Такого каталога/файла не существует!')


def copy_folder():
    """
    Копирование каталога или файла
    """
    old_name = input('Введите имя каталога/файла, который хотите скопировать: ')
    is_dir_exist = False
    while not is_dir_exist:
        if not os.path.exists(old_name):
            old_name = input('Директория не обнаружена! Введите новое имя или наберите "Отмена": ')
            if old_name == 'Отмена':
                return
        else:
            is_dir_exist = True

    new_name = input('Введите новое имя каталога/файла: ')
    old_path = os.path.join(os.getcwd(), old_name)
    new_name = os.path.join(os.getcwd(), new_name)

    # Проверяем есть каталог или нет
    if os.path.exists(old_path):
        # Проверяем каталог это или файл
        shutil.copytree(old_name, new_name) if os.path.isdir(old_path) else shutil.copy(old_name, new_name)
        print('Создан новый каталог/файл: ', os.path.join(os.getcwd(), new_name))
    else:
        print('Исходного каталога/файла не существует!')


def output_list_work_dir_decorator(func):
    """
    Декоратор для функции return_list_work_dir.
    Выводит список построчно
    :param type_output: тип вывода (0 - каталоги и файлы; 1 - только каталоги; 2 - только файлы)
    """
    def inner(type_output = 0):
        if type_output == 0:
            print('Полное содержимое рабочей директории:')
        elif type_output == 1:
            print('Каталоги в рабочей директории:')
        elif type_output == 2:
            print('Файлы в рабочей директории:')

        return_list = func(type_output)
        for element in return_list:
            print(element)

        return return_list

    return inner


@output_list_work_dir_decorator
def return_list_work_dir(type_output = 0):
    """
    Вывод содержимого рабочей директории
    :param type_output: тип вывода (0 - каталоги и файлы; 1 - только каталоги; 2 - только файлы)
    :return: список содержимого
    """
    if type_output == 0:
        return_list = os.listdir()
    elif type_output == 1:
        # Использую генераторы вместо лямбды
        #return_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))
        return_list = [element for element in os.listdir() if os.path.isdir(element)]
    elif type_output == 2:
        # Использую генераторы вместо лямбды
        #return_list = list(filter(lambda x: not os.path.isdir(x), os.listdir()))
        return_list = [element for element in os.listdir() if not os.path.isdir(element)]
    return return_list


# def output_list_work_dir(type_output = 0):
#     """
#     Выводит список построчно
#     :param type_output: тип вывода (0 - каталоги и файлы; 1 - только каталоги; 2 - только файлы)
#     """
#     if type_output == 0:
#         print('Полное содержимое рабочей директории:')
#     elif type_output == 1:
#         print('Каталоги в рабочей директории:')
#     elif type_output == 2:
#         print('Файлы в рабочей директории:')
#
#     return_list = return_list_work_dir(type_output)
#     for element in return_list:
#         print(element)


def save_work_dir_to_file(path):
    """
    Записываем содержимое рабочей директории в текстовый файл: сначала файлы, потом каталоги
    :param path: путь до файла, хранится в настройках, чтобы при смене рабочей директории не менялся.
    """
    with open(path, 'w') as f:
        f.write(f'Содержимое рабочей директории {os.getcwd()}:\n')
        f.write(f'Файлы: {return_list_work_dir(2)}\n')
        f.write(f'Кталоги: {return_list_work_dir(1)}\n')

    return path


def change_work_dir():
    """
    Смена рабочей директории
    """
    new_dir = input("Укажите новую рабочую директорию: ")
    while True:
        if not os.path.exists(new_dir):
            new_dir = input('Директория не обнаружена! Введите полный путь до нее или наберите "Отмена": ')
            if new_dir == 'Отмена':
                break
        else:
            os.chdir(new_dir)
            print('Новая рабочая директория: ', os.path.join(os.getcwd()))
            break