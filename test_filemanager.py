import add_programs.my_account as ma
import functions as fn


def test_add_incomes():
    assert ma.add_incomes(1000, 300) == 1300
    assert ma.add_incomes(0, 500) == 500


def test_subtract_expenses():
    assert ma.subtract_expenses(1000, 300) == 700
    assert ma.subtract_expenses(0, 500) == -500


def test_record_history():
    assert type(ma.record_history([], 'product', 1500)) == list


def test_get_program_info():
    assert fn.get_program_info()['author'] == 'Fomin Dmitry'