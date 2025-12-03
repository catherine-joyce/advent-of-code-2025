from sys import stdin

def get_input():
    total = 0
    for line in stdin:
        numbers_list = list(map(int,line.strip()))
        two_digit_number = get_largest_two_digit_number_in_list(numbers_list)
        total += two_digit_number
    return total

def get_largest_number_in_list(numbers_list):
    return max(numbers_list)

def get_largest_two_digit_number_in_list(numbers_list):
    first_digit = get_largest_number_in_list(numbers_list[0:(len(numbers_list) - 1)])
    second_digit = get_largest_number_in_list(numbers_list[(numbers_list.index(first_digit) + 1):len(numbers_list)])
    result = int(str(first_digit) + str(second_digit))
    return result

if __name__ == "__main__":
    total = get_input()
    print(total)