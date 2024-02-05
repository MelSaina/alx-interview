#!/usr/bin/python3
"""
N-queens puzzle solution
"""

import sys
from typing import List

def is_safe(board: List[int], row: int, col: int) -> bool:
    """Check if it's safe to place a queen in the current position."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board: List[int], n: int) -> None:
    """Print the chessboard configuration for a solution."""
    print([[i, board[i]] for i in range(n)])

def solve_nqueens(board: List[int], row: int, n: int) -> None:
    """Recursively solve the N-queens problem."""
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def main():
    """Main function to handle input and call nqueens function."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()