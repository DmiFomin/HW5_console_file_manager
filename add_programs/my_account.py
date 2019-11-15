import add_programs.my_account_functions as maf


def start_my_account():
    # Получаем настройки программы
    SETTINGS_MY_ACCOUNT = maf.get_my_account_settings()
    # Получаем сохраненный баланс и историю
    balance, history = maf.open_json(SETTINGS_MY_ACCOUNT['name_JSON'])

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            balance = maf.incomes(balance)
        elif choice == '2':
            balance, history = maf.expenses(balance, history)
        elif choice == '3':
            maf.view_history(history)
        elif choice == '4':
            maf.save_json(SETTINGS_MY_ACCOUNT['name_JSON'], balance, history)
            break
        else:
            print('Неверный пункт меню')