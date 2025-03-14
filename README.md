## Sudoku Solver
This is a Python program that solves Sudoku puzzles using the backtracking algorithm. It takes an input grid representing an unsolved Sudoku puzzle and fills in the missing numbers to solve it. The program is designed to handle any valid Sudoku puzzle and will display the completed grid once solved.

## Features
Backtracking Algorithm: Uses a recursive backtracking approach to solve Sudoku puzzles efficiently.

Input Grid: Accepts a 9x9 grid as input, where empty cells are represented by 0.

Validation: Ensures that the solution adheres to Sudoku rules (no duplicates in rows, columns, or 3x3 subgrids).

Readable Output: Displays the solved Sudoku grid in a user-friendly format.

## How to Use
# Clone the Repository (if applicable):

git clone https://github.com/your-username/sudoku-solver.git
cd sudoku-solver

# Run the Program:
Ensure you have Python installed on your system. Then, run the program using the following command:

python3 sudoku_solver.py

# Input the Sudoku Grid:

Modify the grid variable in the main() function to represent your unsolved Sudoku puzzle.

Empty cells should be represented by 0.

# View the Solution:

The program will display the unsolved grid and then the solved grid (if a solution exists).

## Example Input and Output
# Input Grid:

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

Output:
Unsolved Sudoku Grid:
5 3 0 | 0 7 0 | 0 0 0 
6 0 0 | 1 9 5 | 0 0 0 
0 9 8 | 0 0 0 | 0 6 0 
------+-------+------
8 0 0 | 0 6 0 | 0 0 3 
4 0 0 | 8 0 3 | 0 0 1 
7 0 0 | 0 2 0 | 0 0 6 
------+-------+------
0 6 0 | 0 0 0 | 2 8 0 
0 0 0 | 4 1 9 | 0 0 5 
0 0 0 | 0 8 0 | 0 7 9 

Solved Sudoku Grid:
5 3 4 | 6 7 8 | 9 1 2 
6 7 2 | 1 9 5 | 3 4 8 
1 9 8 | 3 4 2 | 5 6 7 
------+-------+------
8 5 9 | 7 6 1 | 4 2 3 
4 2 6 | 8 5 3 | 7 9 1 
7 1 3 | 9 2 4 | 8 5 6 
------+-------+------
9 6 1 | 5 3 7 | 2 8 4 
2 8 7 | 4 1 9 | 6 3 5 
3 4 5 | 2 8 6 | 1 7 9 

## Requirements
Python 3.x

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! If you find any issues or want to improve the program, feel free to open an issue or submit a pull request.

## Author
Joe Brian

https://github.com/JoeB022

joebrian.dev@gmail.com
