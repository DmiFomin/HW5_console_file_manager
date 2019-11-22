import os
import json


def get_my_account_settings():
    """
    Получение настроек
    :return: Словарь с настройками
    """
    settings_my_account = {'name_JSON': os.path.join('add_programs', 'data', 'my_account_data.json')}
    return settings_my_account


def create_json_struct(balance, history):
    """
    Создание структуры JSON
    :return: Возвращает словарь
    """
    json_my_account = {
        'balance': balance,
        'history': history
    }
    return json_my_account


def open_json(path):
    """
    Открывает и считывает JSON, если файла еще нет, то возвращает 0 и пустой список
    :param path: путь до файла
    :return: Возвращает balance (float) и history (list)
    """
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                result = json.load(f)
                balance = result['balance']
                history = result['history']
        except Exception as e:
            print(e)
            print('Ошибка открытия файла')
            balance = 0
            history = []

    else:
        balance = 0
        history = []

    return balance, history


def save_json(path, balance, history):
    """
    Перезаписываем данные в JSON. Если файла нет, то создаем новый.
    :param path: путь до файла
    :param balance: баланс
    :param history: история
    """
    with open(path, 'w') as f:
        json.dump(create_json_struct(balance, history), f)


def add_incomes(balance_f,sum):
    return balance_f + sum


def subtract_expenses(balance_f, sum):
    return balance_f - sum


def record_history(history_f, product, price):
    history_f.append({'product': product, 'price': price})
    return history_f


def incomes(balance_f):
    try:
        add_sum = float(input('Введите сумму для пополнения: '))
    except ValueError:
        print('Нужно ввести число! Попробуйте заново.')
        result = balance_f
    except Exception as e:
        print(e)
        print('Неизвестная ошибка! Попробуйте заново')
        result = balance_f
    else:
        result = add_incomes(balance_f, add_sum)

    return result


def expenses(balance_f, history_f):
    try:
        price = float(input('Введите сумму покупки: '))
    except ValueError:
        print('Нужно ввести число! Попробуйте заново.')
        balance_f = balance_f
        history_f = history_f
    except Exception as e:
        print(e)
        print('Ошибка! Попробуйте заново')
        balance_f = balance_f
        history_f = history_f
    else:
        if price > balance_f:
            print('У вас не хватает средств!')
        else:
            product = input('Что вы хотите купить? ')
            balance_f = subtract_expenses(balance_f, price)
            history_f = record_history(history_f, product, price)

    return balance_f, history_f


def view_history(history_f):
    print('Ваша история покупок:')
    for element in history_f:
        print(f'Товар: {element["product"]}; цена: {element["price"]}')

