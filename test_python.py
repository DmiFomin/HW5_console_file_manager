import math
import os
import shutil


list_for_test = [5, 1, 0, 10, -2, 3, -9, 1]


def test_filter():
    assert list(filter(lambda x: x > 0, list_for_test)) == [5, 1, 10, 3, 1]
    assert list(filter(lambda x: x % 2 == 0, list_for_test)) == [0, 10, -2]


def test_map():
    assert list(map(lambda x: x % 3, list_for_test)) == [2, 1, 0, 1, 1, 0, 0, 1]
    assert list(map(lambda x: x ** 2, list_for_test)) == [25, 1, 0, 100, 4, 9, 81, 1]


def test_sorted():
    assert sorted(list_for_test) == [-9, -2, 0, 1, 1, 3, 5, 10]
    assert sorted(list_for_test, reverse=True) == [10, 5, 3, 1, 1, 0, -2, -9]


def test_pi():
    assert round(math.pi, 2) == 3.14
    assert round(math.pi * 10 ** 2, 2) == 314.16


def test_sqrt():
    assert math.sqrt(16) == 4
    assert math.sqrt(625) == 25


def test_pow():
    assert math.pow(16, 2) == 256
    assert math.pow(-16, 2) == 256


def test_hypot():
    assert round(math.hypot(16, 20), 2) == 25.61
    assert round(math.hypot(-10, 10), 2) == 14.14


def test_copy_file():
    shutil.copy('test_python.py', 'test_python_copy.py')
    assert 'test_python_copy.py' in os.listdir()
