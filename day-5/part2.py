from sys import stdin
import re


def get_fresh_ids_range(id_range):
    id_list = re.findall(r"\d+", id_range)
    return range(int(id_list[0]), int(id_list[1]) + 1)


def check_ranges_overlap(range_1, range_2):
    return (
        (range_1.stop > range_2.start and range_1.start < range_2.stop)
        or (range_1.stop < range_2.start and range_1.start > range_2.stop)
        or (range_1.start >= range_2.start and range_1.stop < range_2.stop)
        or (range_1.start <= range_2.start and range_1.stop > range_2.stop)
    )

def get_number_of_unique_ids(ranges_list):
    count = 0
    consolidated_ranges_list = get_final_consolidated_ranges_list(ranges_list)
    for item in consolidated_ranges_list:
        count += len(item)
    return count

def get_final_consolidated_ranges_list(ranges_list):
    consolidated_ranges_list = get_consolidated_ranges_list(ranges_list)
    ranges_list = recursive_get_consolidated_ranges_list(consolidated_ranges_list)
    second_ranges_list = recursive_get_consolidated_ranges_list(ranges_list)
    return second_ranges_list

    

def recursive_get_consolidated_ranges_list(consolidated_ranges_list):
    final_consolidated_ranges_list = []
    for item in consolidated_ranges_list:
        added = False
        for i in range(len(final_consolidated_ranges_list)):
            existing_range = final_consolidated_ranges_list[i]
            if check_ranges_overlap(item, existing_range) and not added:
                final_consolidated_ranges_list[i] = range(
                    min(item.start, existing_range.start),
                    max(item.stop, existing_range.stop),
                )
                added = True
        if not added:
            final_consolidated_ranges_list.append(item)
    return final_consolidated_ranges_list

def get_consolidated_ranges_list(ranges_list):
    consolidated_ranges_list = []
    for item in ranges_list:
        id_range = get_fresh_ids_range(item)
        added = False
        for i in range(len(consolidated_ranges_list)):
            existing_range = consolidated_ranges_list[i]
            if check_ranges_overlap(id_range, existing_range) and not added:
                consolidated_ranges_list[i] = range(
                    min(id_range.start, existing_range.start),
                    max(id_range.stop, existing_range.stop),
                )
                added = True
        if not added:
            consolidated_ranges_list.append(id_range)
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
    answer = get_number_of_unique_ids(ranges_list)
    print(answer)
