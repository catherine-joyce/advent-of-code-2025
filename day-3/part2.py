from sys import stdin

def get_largest_number_and_index_in_list(numbers_list):
    return max(numbers_list), numbers_list.index(max(numbers_list))

def get_largest_twelve_digit_number_in_list(numbers_list):
    result_string = ""
    start = 0
    for i in range(11, -1, -1):
        digit, digit_index = get_largest_number_and_index_in_list(numbers_list[start:(len(numbers_list) - i)])
        start += digit_index + 1
        result_string += str(digit)     
    return int(result_string)

def get_input_and_total():
    total = 0
    for line in stdin:
        numbers_list = list(map(int,line.strip()))
        twelve_digit_number = get_largest_twelve_digit_number_in_list(numbers_list)
        total += twelve_digit_number
    return total

if __name__ == "__main__":
    total = get_input_and_total()
    print(total)