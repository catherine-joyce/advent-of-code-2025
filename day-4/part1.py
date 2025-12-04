from sys import stdin

def get_input_and_create_grid():
    grid = []
    for line in stdin:
        row = list(line.strip())
        grid.append(row)
    return grid

grid = get_input_and_create_grid()