from part1 import check_ids_and_get_count, get_fresh_ids_range


def test_check_count_fresh_ids():
    numbers_to_check = {32, 1, 5, 8, 11, 17}
    ranges_list = ["3-5", "10-14", "16-20", "12-18"]
    count = check_ids_and_get_count(numbers_to_check, ranges_list)
    assert count == 3


def test_get_range_object():
    id_range = "12-18"
    range_object = get_fresh_ids_range(id_range)
    assert range_object == range(12, 19)
