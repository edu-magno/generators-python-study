from main import *
from asserts_lists import *


file_path = 'mini_profiles.csv'


def test_find_profiles_between_20_and_35_years():
    result = find_profiles_between_20_and_35_years(file_path)
    expected = expected_ex1

    assert expected == list(result)


def test_find_select_blood_donors_1():
    result = find_select_blood_donors_1(file_path)
    expected = expected_ex2

    assert expected == list(result)


def test_find_select_blood_donors_2():
    result = find_select_blood_donors_2(file_path)
    expected = expected_ex3

    assert expected == list(result)


def test_find_select_blood_donors_3():
    result = find_select_blood_donors_3(file_path)
    expected = expected_ex4

    assert expected == list(result)
