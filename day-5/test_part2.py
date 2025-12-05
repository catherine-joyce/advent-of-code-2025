from part2 import get_consolidated_ranges_list, check_ranges_overlap, get_final_consolidated_ranges_list, get_number_of_unique_ids


def test_get_consolidated_ranges_list():
    ranges_list = ["3-5", "10-14", "16-20", "12-18"]
    consolidated_ranges_list = get_final_consolidated_ranges_list(ranges_list)
    assert consolidated_ranges_list == [range(3, 6), range(10, 21)]

def test_get_number_of_unique_ids():
    count = 0
    ranges_list = ["3-5", "10-14", "16-20", "12-18"]
    result = get_number_of_unique_ids(ranges_list)
    assert result == 14

def test_check_ranges_overlap_true():
    range1 = range(10, 15)
    range2 = range(12, 19)
    result = check_ranges_overlap(range1, range2)
    assert result


def test_check_ranges_overlap_false():
    range1 = range(3, 6)
    range2 = range(12, 19)
    result = check_ranges_overlap(range1, range2)
    assert not result


def test_check_ranges_overlap_false_case_2():
    range1 = range(3, 7)
    range2 = range(8, 19)
    result = check_ranges_overlap(range1, range2)
    assert not result


def test_check_ranges_overlap_true_case_2():
    range1 = range(13, 17)
    range2 = range(12, 19)
    result = check_ranges_overlap(range1, range2)
    assert result


def test_check_ranges_overlap_true_case_3():
    range1 = range(17, 20)
    range2 = range(12, 19)
    result = check_ranges_overlap(range1, range2)
    assert result 

def test_check_ranges_overlap_true_case_4():
    range1 = range(13, 15)
    range2 = range(12, 19)
    result = check_ranges_overlap(range1, range2)
    assert result 

def test_check_ranges_overlap_true_case_5():
    range1 = range(1, 20)
    range2 = range(4, 7)
    result = check_ranges_overlap(range1, range2)
    assert result 


def test_check_ranges_overlap_true_case_6():
    range1 = range(1, 9)
    range2 = range(8, 19)
    result = check_ranges_overlap(range1, range2)
    assert result


def test_check_ranges_overlap_true_case_7():
    range1 = range(7, 21)
    range2 = range(3, 18)
    result = check_ranges_overlap(range1, range2)
    assert result 

def test_check_ranges_overlap_false_case_3():
    range1 = range(1, 4)
    range2 = range(4, 8)
    result = check_ranges_overlap(range1, range2)
    assert not result 

def test_check_ranges_overlap_false_case_4():
    range1 = range(15, 20)
    range2 = range(11, 15)
    result = check_ranges_overlap(range1, range2)
    assert not result 