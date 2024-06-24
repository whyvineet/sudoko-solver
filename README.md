# Sudoku Solver

This Python code is designed to solve Sudoku puzzles using the backtracking algorithm. The backtracking approach systematically searches for a solution by trying each possible number in each empty cell and backtracking whenever it encounters a conflict. If a valid solution exists for the given Sudoku puzzle, the algorithm will find it. If the puzzle is unsolvable, the algorithm will determine that no solution exists.

## What is Backtracking Algorithm?

**Backtracking** is a problem-solving algorithmic technique that involves finding a solution incrementally by trying **different options** and **undoing** them if they lead to a **dead end**.

It is commonly used in situations where you need to explore multiple possibilities to solve a problem, like searching for a path in a maze or solving puzzles like  ****Sudoku**** . When a dead end is reached, the algorithm backtracks to the previous decision point and explores a different path until a solution is found or all possibilities have been exhausted. ([GeeksForGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/))

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/whyvineet/sudoku-solver.git
   cd sudoku-solver
   ```
2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
    python -m venv venv
    # On macOS/Linux
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
   ```

## Usage

1. **Run the Sudoku Solver**

   ```bash
   python main.py
   ```

## File Stucture

```
sudoku-solver/
│
├── main.py               # Main script to run the Sudoku solver
├── README.md             # Readme file
├── LICENSE               # License file
└── .gitignore            # Gitignore file
```

## License

This project is licensed under the Unlicense License. See the [LICENSE](./LICENSE) file for more details.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me at [whyvineet@outlook.com](mailto:whyvineet@outlook.com).

---

Thank you for using Sudoku Solver! Happy coding!

---

Feel free to modify and extend this project as per your needs. Contributions are highly appreciated.
