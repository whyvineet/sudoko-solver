def is_valid_move(grid, row, col, number):
    for i in range(9):
        if grid[row][i] == number:
            return False
    
    for i in range(9):
        if grid[i][col] == number:
            return False
        
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == number:
                return False
    return True

def solve_sudoku(grid, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for number in range(1, 10, 1):
        if is_valid_move(grid, row, col, number):
            grid[row][col] = number
            if solve_sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = " ")
        print()
    
grid = [[1, 0, 0, 0, 0, 0, 9, 5, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 8, 6, 1, 5, 9, 0, 0, 0],
        [8, 0, 3, 0, 2, 4, 0, 0, 0],
        [0, 0, 0, 3, 8, 0, 0, 6, 2],
        [0, 2, 1, 0, 0, 0, 0, 0, 3],
        [0, 0, 5, 0, 3, 6, 0, 1, 0],
        [2, 3, 0, 7, 0, 5, 0, 0, 9],
        [0, 0, 0, 0, 4, 0, 0, 0, 5]]

if solve_sudoku(grid, 0, 0):
    print_grid(grid)
else:
    print("No solution exists")