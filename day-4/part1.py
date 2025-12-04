from sys import stdin

def get_input_and_create_grid():
    grid = []
    for line in stdin:
        row = list(line.strip())
        grid.append(row)
    return grid

def check_adjacent_squares(grid, row, square_position):
    adjacent_squares_list = []
    if row == 0 and square_position != len(grid[row]) -1 :
        middle_left = grid[row][square_position - 1]
        middle_right = grid[row][square_position + 1]
        bottom_left = grid[row + 1][square_position - 1]
        bottom_middle = grid[row +1][square_position]
        bottom_right = grid[row +1][square_position + 1]
        adjacent_squares_list.append(middle_left)
        adjacent_squares_list.append(middle_right)
        adjacent_squares_list.append(bottom_left)
        adjacent_squares_list.append(bottom_middle)
        adjacent_squares_list.append(bottom_right)
    elif row == 0 and square_position == len(grid[row]) -1 :
        middle_left = grid[row][square_position - 1]
        bottom_left = grid[row + 1][square_position - 1]
        bottom_middle = grid[row +1][square_position]
        adjacent_squares_list.append(middle_left)
        adjacent_squares_list.append(bottom_left)
        adjacent_squares_list.append(bottom_middle)
    elif row == len(grid)-1 and square_position != len(grid[row]) -1:
        top_left = grid[row - 1][square_position - 1]
        top_middle = grid[row - 1][square_position]
        top_right = grid[row - 1][square_position + 1]
        middle_left = grid[row][square_position - 1]
        middle_right = grid[row][square_position + 1]
        adjacent_squares_list.append(top_left)
        adjacent_squares_list.append(top_middle)
        adjacent_squares_list.append(top_right)
        adjacent_squares_list.append(middle_left)
        adjacent_squares_list.append(middle_right)
    elif row == len(grid)-1 and square_position == len(grid[row]) -1:
        top_left = grid[row - 1][square_position - 1]
        top_middle = grid[row - 1][square_position]
        middle_left = grid[row][square_position - 1]
        adjacent_squares_list.append(top_left)
        adjacent_squares_list.append(top_middle)
        adjacent_squares_list.append(middle_left)
    elif square_position == 0:
        top_middle = grid[row - 1][square_position]
        top_right = grid[row - 1][square_position + 1]
        middle_right = grid[row][square_position + 1]
        bottom_middle = grid[row +1][square_position]
        bottom_right = grid[row +1][square_position + 1]
        adjacent_squares_list.append(top_middle)
        adjacent_squares_list.append(top_right)
        adjacent_squares_list.append(middle_right)
        adjacent_squares_list.append(bottom_middle)
        adjacent_squares_list.append(bottom_right)
    elif square_position == len(grid[row]) -1:
        top_left = grid[row - 1][square_position - 1]
        top_middle = grid[row - 1][square_position]
        middle_left = grid[row][square_position - 1]
        bottom_left = grid[row + 1][square_position - 1]
        bottom_middle = grid[row +1][square_position]
        adjacent_squares_list.append(top_left)
        adjacent_squares_list.append(top_middle)
        adjacent_squares_list.append(middle_left)
        adjacent_squares_list.append(bottom_left)
        adjacent_squares_list.append(bottom_middle)
    else:
        top_left = grid[row - 1][square_position - 1]
        top_middle = grid[row - 1][square_position]
        top_right = grid[row - 1][square_position + 1]
        middle_left = grid[row][square_position - 1]
        middle_right = grid[row][square_position + 1]
        bottom_left = grid[row + 1][square_position - 1]
        bottom_middle = grid[row +1][square_position]
        bottom_right = grid[row +1][square_position + 1]
        adjacent_squares_list.append(top_left)
        adjacent_squares_list.append(top_middle)
        adjacent_squares_list.append(top_right)
        adjacent_squares_list.append(middle_left)
        adjacent_squares_list.append(middle_right)
        adjacent_squares_list.append(bottom_left)
        adjacent_squares_list.append(bottom_middle)
        adjacent_squares_list.append(bottom_right)
    return adjacent_squares_list






if __name__ == "__main__":
    grid = get_input_and_create_grid()
    number_of_rolls = 0
    for row in range(len(grid)):
        for square in range(len(grid[row])):
            if grid[row][square] == "@":
                adjacent_squares_list = check_adjacent_squares(grid, row, square) 
                if len([x for x in adjacent_squares_list if x == "@"]) < 4:
                    number_of_rolls += 1
    print(number_of_rolls)

