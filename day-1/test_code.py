from part1 import create_numbers_list, get_new_number, get_number_of_zeros

def test_get_82_from_L68():
    text_input = 'L68'
    current_number = 50
    numbers = create_numbers_list()
    new_number = get_new_number(numbers, current_number, text_input)
    assert new_number == 82

def test_get_0_from_R48():
    text_input = 'R48'
    current_number = 52
    numbers = create_numbers_list()
    new_number = get_new_number(numbers, current_number, text_input)
    assert new_number == 0

def test_get_32_from_list():
    list_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    current_number = 50
    numbers = create_numbers_list()
    for element in list_input:
        current_number = get_new_number(numbers, current_number, element)
    assert current_number == 32

def test_number_of_zeros():
    list_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    current_number = 50
    numbers = create_numbers_list()
    result = get_number_of_zeros(numbers, current_number, list_input)
    assert result == 3
