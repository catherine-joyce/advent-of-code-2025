from part1 import get_number_of_invalid_ids

def test_2_invalid_ids():
    number, invalid_list = get_number_of_invalid_ids("11-22")
    assert number == 2
    assert invalid_list == [11, 22]

def test_1_invalid_ids():
    number, invalid_list = get_number_of_invalid_ids("95-115")
    assert number == 1
    assert invalid_list == [99]

def test_1_invalid_ids_case_2():
    number, invalid_list = get_number_of_invalid_ids("998-1012")
    assert number == 1
    assert invalid_list == [1010]

def test_1_invalid_ids_case_3():
    number, invalid_list = get_number_of_invalid_ids("1188511880-1188511890")
    assert number == 1
    assert invalid_list == [1188511885]

def test_1_invalid_ids_case_4():
    number, invalid_list = get_number_of_invalid_ids("222220-222224")
    assert number == 1
    assert invalid_list == [222222]

def test_0_invalid_ids():
    number, invalid_list = get_number_of_invalid_ids("1698522-1698528")
    assert number == 0
    assert invalid_list == []

def test_1_invalid_ids_case_5():
    number, invalid_list = get_number_of_invalid_ids("446443-446449")
    assert number == 1
    assert invalid_list == [446446]

def test_1_invalid_ids_case_6():
    number, invalid_list = get_number_of_invalid_ids("38593856-38593862")
    assert number == 1
    assert invalid_list == [38593859]

def test_0_invalid_ids_case_2():
    number, invalid_list = get_number_of_invalid_ids("824824821-824824827")
    assert number == 0
    assert invalid_list == []
