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
    positions_list = []
    for row in range(len(grid)):
        for square in range(len(grid[row])):
            if grid[row][square] == "@":
                adjacent_squares_list = check_adjacent_squares(grid, row, square) 
                if len([x for x in adjacent_squares_list if x == "@"]) < 4:
                    number_of_rolls += 1
                    positions_list.append([row, square])
    return number_of_rolls, positions_list

def remove_rolls(grid, positions_list):
    for position in positions_list:
        grid[position[0]][position[1]] = "."
    return grid

def get_total_rolls(grid):
    done = False
    total = 0
    while not done:
        number_of_rolls, positions_list = get_num_of_rolls(grid)
        total += number_of_rolls
        if number_of_rolls == 0:
            done = True
        grid = remove_rolls(grid, positions_list)
    return total



if __name__ == "__main__":
    grid = get_input_and_create_grid()
    total = get_total_rolls(grid)
    print(total)
    


