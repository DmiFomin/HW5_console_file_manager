import functions as fn

while True:
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        fn.create_folder()
    elif choice == '2':
        fn.delete_folder()
    elif choice == '3':
        fn.copy_folder()
    elif choice == '4':
        fn.output_list_work_dir()
    elif choice == '5':
        fn.output_list_work_dir(1)
    elif choice == '6':
        fn.output_list_work_dir(2)
    elif choice == '7':
        pass
    elif choice == '8':
        pass
    elif choice == '9':
        pass
    elif choice == '10':
        pass
    elif choice == '11':
        fn.change_work_dir()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')