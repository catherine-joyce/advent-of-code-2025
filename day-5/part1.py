from sys import stdin
import re


def get_fresh_ids_range(id_range):
    id_list = re.findall(r"\d+", id_range)
    return range(int(id_list[0]), int(id_list[1]) + 1)


def check_ids_and_get_count(numbers_to_check, ranges_list):
    count = 0
    found_numbers = set()
    for item in ranges_list:
        id_range = get_fresh_ids_range(item)
        for number in numbers_to_check:
            if number in id_range and number not in found_numbers:
                count += 1
                found_numbers.add(number)
    return count


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
