from part2 import get_consolidated_ranges_list, check_ranges_overlap


# def test_get_consolidated_ranges_list():
#     ranges_list = ["3-5", "10-14", "16-20", "12-18"]
#     consolidated_ranges_list = get_consolidated_ranges_list(ranges_list)
#     assert consolidated_ranges_list == [range(3, 6), range(10, 21)]


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
