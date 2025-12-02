from part2 import get_number_of_invalid_ids_part_2

def test_2_invalid_ids_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("11-22")
    assert number == 2
    assert invalid_list == [11, 22]

def test_2_invalid_ids_case_2_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("95-115")
    assert number == 2
    assert invalid_list == [99, 111]

def test_2_invalid_ids_case_3_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("998-1012")
    assert number == 2
    assert invalid_list == [999, 1010]

def test_1_invalid_ids_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("1188511880-1188511890")
    assert number == 1
    assert invalid_list == [1188511885]

def test_1_invalid_ids_case_2_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("222220-222224")
    assert number == 1
    assert invalid_list == [222222]

def test_0_invalid_ids_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("1698522-1698528")
    assert number == 0
    assert invalid_list == []

def test_1_invalid_ids_case_3_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("446443-446449")
    assert number == 1
    assert invalid_list == [446446]

def test_1_invalid_ids_case_4_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("38593856-38593862")
    assert number == 1
    assert invalid_list == [38593859]

def test_1_invalid_ids_case_5_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("565653-565659")
    assert number == 1
    assert invalid_list == [565656]

def test_1_invalid_ids_case_6_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("824824821-824824827")
    assert number == 1
    assert invalid_list == [824824824]

def test_1_invalid_ids_case_7_part_2():
    number, invalid_list = get_number_of_invalid_ids_part_2("2121212118-2121212124")
    assert number == 1
    assert invalid_list == [2121212121]

