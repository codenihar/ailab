def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row] = 0  # Backtrack

def solve_n_queens(n):
    board = [0] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_solution(solution):
    for row in solution:
        queens_row = ['.'] * len(solution)
        queens_row[row] = 'Q'
        print(" ".join(queens_row))
    print()

if __name__ == "__main__":
    n = 4  # Change this value for different board sizes
    solutions = solve_n_queens(n)

    print(f"Solutions for {n}-Queens problem:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        print_solution(solution)
