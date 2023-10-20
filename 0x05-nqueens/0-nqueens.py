#!/usr/bin/python3
def nqueens(n):
  """
  Finds all possible ways to place n queens on an n×n chessboard such that no two queens attack each other.

  Args:
    n: The number of queens.

  Returns:
    A list of all possible placements of the queens.
  """
  solutions = []
  def backtrack(row, queens):
    if row == n:
      solutions.append(queens)
      return
    for i in range(n):
      if is_valid(row, i, queens):
        queens.append((row, i))
        backtrack(row + 1, queens)
        queens.pop()
  backtrack(0, [])
  return solutions

def is_valid(row, col, queens):
  """
  Checks if a queen can be placed at the given row and column.

  Args:
    row: The row of the queen.
    col: The column of the queen.
    queens: A list of all the queens that have already been placed.

  Returns:
    True if the queen can be placed at the given row and column, False otherwise.
  """
  for queen in queens:
    if queen[0] == row or queen[1] == col or abs(queen[0] - row) == abs(queen[1] - col):
      return False
  return True
