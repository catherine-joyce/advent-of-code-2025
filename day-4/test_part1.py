from part1 import check_adjacent_squares

grid = [
    ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'], 
    ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'], 
    ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'], 
    ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'], 
    ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'], 
    ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'], 
    ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'], 
    ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'], 
    ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'], 
    ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.']
    ]

def test_fewer_than_four_rolls():
    squares_list = check_adjacent_squares(grid, 2, 6)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_2():
    squares_list = check_adjacent_squares(grid, 0, 2)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_3():
    squares_list = check_adjacent_squares(grid, 0, 3)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_4():
    squares_list = check_adjacent_squares(grid, 0, 5)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_5():
    squares_list = check_adjacent_squares(grid, 0, 6)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_6():
    squares_list = check_adjacent_squares(grid, 0, 8)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_7():
    squares_list = check_adjacent_squares(grid, 1, 0)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_8():
    squares_list = check_adjacent_squares(grid, 4, 0)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_9():
    squares_list = check_adjacent_squares(grid, 4, 9)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_10():
    squares_list = check_adjacent_squares(grid, 7, 0)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_11():
    squares_list = check_adjacent_squares(grid, 9, 0)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_12():
    squares_list = check_adjacent_squares(grid, 9, 2)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_fewer_than_four_rolls_case_13():
    squares_list = check_adjacent_squares(grid, 9, 8)
    assert len([x for x in squares_list if x == "@"]) < 4

def test_equal_or_more_than_four_rolls():
    squares_list = check_adjacent_squares(grid, 0, 7)
    assert len([x for x in squares_list if x == "@"]) >= 4

def test_equal_or_more_than_four_rolls_case_2():
    squares_list = check_adjacent_squares(grid, 1, 9)
    assert len([x for x in squares_list if x == "@"]) >= 4 