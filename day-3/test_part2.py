from part2 import get_largest_twelve_digit_number_in_list

def test_find_largest_twelve_digit_number_in_list():
    numbers_list = [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1]
    result = get_largest_twelve_digit_number_in_list(numbers_list)
    assert result == 987654321111

def test_find_largest_twelve_digit_number_in_list_case_2():
    numbers_list = [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9]
    result = get_largest_twelve_digit_number_in_list(numbers_list)
    assert result == 811111111119

def test_find_largest_twelve_digit_number_in_list_case_3():
    numbers_list = [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8]
    result = get_largest_twelve_digit_number_in_list(numbers_list)
    assert result == 434234234278

def test_find_largest_twelve_digit_number_in_list_case_4():
    numbers_list = [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1]
    result = get_largest_twelve_digit_number_in_list(numbers_list)
    assert result == 888911112111