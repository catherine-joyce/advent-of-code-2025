from sys import stdin
import re


def get_fresh_ids_range(id_range):
    id_list = re.findall(r"\d+", id_range)
    return range(int(id_list[0]), int(id_list[1]) + 1)


def check_ranges_overlap(range_1, range_2):
    return (
        (range_1.stop >= range_2.start and range_1.start <= range_2.stop)
        or (range_1.stop <= range_2.start and range_1.start >= range_2.stop)
        or (range_1.start >= range_2.start and range_1.stop < range_2.stop)
        or (range_1.start <= range_2.start and range_1.stop > range_2.stop)
    )


def get_consolidated_ranges_list(ranges_list):
    consolidated_ranges_list = []
    for item in ranges_list:
        id_range = get_fresh_ids_range(item)
        for i in range(len(consolidated_ranges_list)):
            existing_range = consolidated_ranges_list[i]
            if check_ranges_overlap(id_range, consolidated_ranges_list[i]):
                consolidated_ranges_list[i] = range(
                    min(id_range.start, existing_range.start),
                    max(id_range.stop, existing_range.stop),
                )
    return consolidated_ranges_list


def get_numbers_and_ranges_input():
    numbers_to_check = set()
    ranges_list = []
    for line in stdin:
        item = line.strip()
        if "-" not in item and item != "":
            numbers_to_check.add(int(item))
        if "-" in item:
            ranges_list.append(item)
    return numbers_to_check, ranges_list


if __name__ == "__main__":
    numbers_list, ranges_list = get_numbers_and_ranges_input()
    print(numbers_list)
    print(ranges_list)
    answer = check_ids_and_get_count(numbers_list, ranges_list)
    print(answer)
