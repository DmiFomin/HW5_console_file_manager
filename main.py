import functions as fn
import add_programs.victory as vk
import add_programs.my_account as ma

# Записываем в константу информацию об программе
PROGRAM_INFO = fn.get_program_info()

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
        print('Информация об перационной системе: ', PROGRAM_INFO['OS'])
    elif choice == '8':
        print('Автор программы: ', PROGRAM_INFO['author'])
    elif choice == '9':
        vk.start_victory()
    elif choice == '10':
        ma.start_my_account()
    elif choice == '11':
        fn.change_work_dir()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')