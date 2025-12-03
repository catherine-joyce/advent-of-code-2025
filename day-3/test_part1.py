from part1 import get_largest_number_in_list, get_largest_two_digit_number_in_list

def test_find_largest_number_in_list():
    numbers_list = [9,8,7,6,5,4,3,2,1,1,1,1,1,1]
    result = get_largest_number_in_list(numbers_list)
    assert result == 9

def test_find_largest_number_in_list_case_2():
    numbers_list = [8,7,6,5,4,3,2,1,1,1,1,1,1,1]
    result = get_largest_number_in_list(numbers_list)
    assert result == 8

def test_find_largest_number_in_list_case_3():
    numbers_list = [8,1,1,1,1,1,1,1,1,1,1,1,1,1]
    result = get_largest_number_in_list(numbers_list)
    assert result == 8

def test_find_largest_number_in_list_case_4():
    numbers_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,9]
    result = get_largest_number_in_list(numbers_list)
    assert result == 9

def test_find_largest_two_digit_number_in_list():
    numbers_list = [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1]
    result = get_largest_two_digit_number_in_list(numbers_list)
    assert result == 98

def test_find_largest_two_digit_number_in_list_case_2():
    numbers_list = [8,7,6,5,4,3,2,1,1,1,1,1,1,1,9]
    result = get_largest_two_digit_number_in_list(numbers_list)
    assert result == 89

def test_find_largest_two_digit_number_in_list_case_3():
    numbers_list = [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8]
    result = get_largest_two_digit_number_in_list(numbers_list)
    assert result == 78

def test_find_largest_two_digit_number_in_list_case_4():
    numbers_list = [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]
    result = get_largest_two_digit_number_in_list(numbers_list)
    assert result == 92