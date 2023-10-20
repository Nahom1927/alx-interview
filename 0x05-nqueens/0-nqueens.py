#!/usr/bin/python3
def n_queens(n):
  """Solve the n-queens problem.

  Args:
    n: The number of queens.

  Returns:
    A list of lists, where each inner list represents a row of the chessboard, and
    each queen is represented by a 'Q'.
  """
  if n <= 0:
    return []

  # Initialize the board to all empty squares.
  board = [['.' for _ in range(n)] for _ in range(n)]

  # Recursively place the queens on the board.
  def place_queens(row, queens_placed):
    if row == n:
      return True

    for col in range(n):
      if is_valid(board, row, col):
        board[row][col] = 'Q'
        if place_queens(row + 1, queens_placed + 1):
          return True

        board[row][col] = '.'

    return False

  return place_queens(0, 0)

def is_valid(board, row, col):
  """Check if the given position is valid for a queen.

  Args:
    board: The board.
    row: The row of the queen.
    col: The column of the queen.

  Returns:
    True if the position is valid, False otherwise.
  """
  # Check if the queen is in the same row as another queen.
  for i in range(row):
    if board[i][col] == 'Q':
      return False

  # Check if the queen is in the same column as another queen.
  for i in range(n):
    if board[row][i] == 'Q':
      return False

  # Check if the queen is in the same diagonal as another queen.
  for i in range(-row, row + 1):
    for j in range(-col, col + 1):
      if i != 0 and j != 0:
        if board[row + i][col + j] == 'Q':
          return False

  return True
