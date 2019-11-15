import os
import add_programs.my_account_functions as maf
import functions as fn


# Проверяем функцию увеличения баланса
def test_add_incomes():
    assert maf.add_incomes(1000, 300) == 1300
    assert maf.add_incomes(0, 500) == 500


# Проверяем функцию уменьшения баланса
def test_subtract_expenses():
    assert maf.subtract_expenses(1000, 300) == 700
    assert maf.subtract_expenses(0, 500) == -500


# Проверяем тип истории
def test_record_history():
    assert type(maf.record_history([], 'product', 1500)) == list


# Проверяем получение информации о программе console_file_manager
def test_get_program_info():
    assert fn.get_program_info()['author'] == 'Fomin Dmitry'


# Проверяем получение настроек в my_account
def test_get_my_accout_settings():
    assert maf.get_my_accout_settings()['name_JSON'] == os.path.join('data','my_account_data.json')


# Проверяем структуру json
def test_create_json_struct():
    assert type(maf.create_json_struct(25.5, ['product: "milk"', 'price: 60'])) == dict
    assert len(maf.create_json_struct(25.5, ['product: "milk"', 'price: 60'])) == 2