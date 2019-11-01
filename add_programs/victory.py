import random

def start_victory():
    list_of_person = []

    list_of_person.append({'name': 'Никола Тесла', 'date_of_birth': '10.07.1856', 'date_of_birth_str': 'десятое июля 1856 года'})
    list_of_person.append({'name': 'Дмитрий Иванович Менделеев', 'date_of_birth': '27.01.1834', 'date_of_birth_str': 'двадцать седьмое января 1834 года'})
    list_of_person.append({'name': 'Иван Петрович Павлов', 'date_of_birth': '14.09.1849', 'date_of_birth_str': 'четырнадцатое сентября 1849 года'})
    list_of_person.append({'name': 'Томас Эдисон', 'date_of_birth': '11.02.1847', 'date_of_birth_str': 'одиннадцатое февраля 1847 года'})
    list_of_person.append({'name': 'Мария Склодовская-Кюри', 'date_of_birth': '07.11.1867', 'date_of_birth_str': 'седьмое ноября 1867 года'})
    list_of_person.append({'name': 'Илон Маск', 'date_of_birth': '28.06.1971', 'date_of_birth_str': 'двадцать восьмое июня 1971 года'})
    list_of_person.append({'name': 'Альберт Эйнштейн', 'date_of_birth': '14.03.1879', 'date_of_birth_str': 'четырнадцатое марта 1879 года'})
    list_of_person.append({'name': 'Чарльз Дарвин', 'date_of_birth': '12.02.1809', 'date_of_birth_str': 'двенадцатое февраля 1809 года'})
    list_of_person.append({'name': 'Владимир Николаевич Челомей', 'date_of_birth': '17.06.1914', 'date_of_birth_str': 'семнадцатое июня 1914 года'})
    list_of_person.append({'name': 'Сергей Павлович Королёв', 'date_of_birth': '30.12.1906', 'date_of_birth_str': 'тридцатое декабря 1906 года'})

    again = 'Да'

    while again == 'Да':

        count_true = 0;
        count_false = 0;
        percent_true = 0
        percent_false = 0

        print('Вам нужно правильно ввести дату рождения изместных людей в формате dd.mm.yyyy.')
        count_questions = input(f'Укажите количество вопросов, на которые хотите ответить (от 1 до {len(list_of_person)}): ')

        list_for_output = random.sample(list_of_person, int(count_questions))

        for question in list_for_output:
            user_answer = input(question['name'] + ': ')
            if user_answer != question['date_of_birth']:
                #print('Неверно! Правильный ответ: {}'.format(date_to_string(question['date_of_birth'])))
                print('Неверно! Правильный ответ: {}'.format(question['date_of_birth_str']))
                count_false += 1
            else:
                count_true += 1

        percent_true = count_true * 100 / int(count_questions)
        percent_false = count_false * 100 / int(count_questions)

        if (percent_true == 100):
            print('Вы ответили на все вопросы правильно!')
        elif (percent_false == 100):
            print('Вы не угадали ни одной даты рождения!')
        else:
            print('Правильные ответы: ', str(percent_true), ';', 'Неправильные ответы', str(percent_false))

        again = input('Будете играть еще? ')

    print('Игра закончена!')

