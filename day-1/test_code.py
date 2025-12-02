from part1 import get_new_number, get_number_of_zeros

from part2 import get_number_of_zeros_part_2, get_new_number_part_2

def test_get_82_from_L68():
    text_input = 'L68'
    current_number = 50
    new_number = get_new_number(current_number, text_input)
    assert new_number == 82

def test_get_0_from_R48():
    text_input = 'R48'
    current_number = 52
    new_number = get_new_number(current_number, text_input)
    assert new_number == 0

def test_get_32_from_list():
    list_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    current_number = 50
    for element in list_input:
        current_number = get_new_number(current_number, element)
    assert current_number == 32

def test_number_of_zeros():
    list_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    current_number = 50
    result = get_number_of_zeros(current_number, list_input)
    assert result == 3

def test_number_of_zeros_part_2():
    list_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    current_number = 50
    result = get_number_of_zeros_part_2(current_number, list_input)
    assert result == 6

def test_get_82_from_L68_part_2_zero_count():
    text_input = 'L68'
    current_number = 50
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 82
    assert zero_count == 1

def test_get_0_from_R48_part_2_zero_count():
    text_input = 'R48'
    current_number = 52
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 0
    assert zero_count == 0

def test_part_2_zero_count_from_R446():
    text_input = 'R446'
    current_number = 50
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 96
    assert zero_count == 4

def test_part_2_zero_count_from_L665():
    text_input = 'L665'
    current_number = 50
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 85
    assert zero_count == 7

def test_part_2_zero_count_from_R1000():
    text_input = 'R1000'
    current_number = 50
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 50
    assert zero_count == 10

def test_part_2_zero_count_from_L250():
    text_input = 'L250'
    current_number = 10
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 60
    assert zero_count == 3 

def test_part_2_zero_count_from_L250_with_starting_number_50():
    text_input = 'L250'
    current_number = 50
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 0
    assert zero_count == 2

def test_part_2_zero_count_from_R250_with_starting_number_50():
    text_input = 'R250'
    current_number = 50
    new_number, zero_count = get_new_number_part_2(current_number, text_input)
    assert new_number == 0
    assert zero_count == 2