def print_grid(grid):
    """Print the Sudoku grid in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()

def find_empty(grid):
    """Find the next empty cell (represented by 0) in the grid."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # Row, column
    return None

def is_valid(grid, num, pos):
    """Check if placing `num` at position `pos` is valid."""
    # Check row
    for j in range(9):
        if grid[pos[0]][j] == num and pos[1] != j:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty(grid)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0  # Backtrack

    return False

def main():
    """Main function to solve a Sudoku puzzle."""
    # Example unsolved Sudoku grid (0 represents empty cells)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku Grid:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSolved Sudoku Grid:")
        print_grid(grid)
    else:
        print("No solution exists for this Sudoku puzzle.")

if __name__ == "__main__":
    main()