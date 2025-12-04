from sys import stdin

def get_input_and_create_grid():
    grid = []
    for line in stdin:
        row = list(line.strip())
        grid.append(row)
    return grid

def check_adjacent_squares(grid, row, square_position):
    adjacent_squares_list = []
    positions_list = [
        [(row - 1), (square_position - 1)], 
        [(row - 1), (square_position)], 
        [(row - 1), (square_position + 1)],
        [(row), (square_position - 1)], 
        [(row), (square_position + 1)],
        [(row + 1), (square_position - 1)], 
        [(row + 1), (square_position)], 
        [(row + 1), (square_position + 1)],
        ]
    relevant_positions_list = [x for x in positions_list if (x[0] >= 0) and (x[1] >= 0) and (x[0] < len(grid))and (x[1] < len(grid[0]))]
    for position in relevant_positions_list:
        adjacent_squares_list.append(grid[position[0]][position[1]])
    return adjacent_squares_list

def get_num_of_rolls(grid):
    number_of_rolls = 0
    for row in range(len(grid)):
        for square in range(len(grid[row])):
            if grid[row][square] == "@":
                adjacent_squares_list = check_adjacent_squares(grid, row, square) 
                if len([x for x in adjacent_squares_list if x == "@"]) < 4:
                    number_of_rolls += 1
    return number_of_rolls

if __name__ == "__main__":
    grid = get_input_and_create_grid()
    number_of_rolls = get_num_of_rolls(grid)
    print(number_of_rolls)

