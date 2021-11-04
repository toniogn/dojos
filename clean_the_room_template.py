from typing import List

def cleanable_squares_number(grid: List[str]) -> int:
  """Count the number of cleanable squares of a given grid.
  
  Parameters
  ----------
  grid : List[str]
    Grid containing empty (".") or occupied squares ("x").
    
  Returns
  -------
  int
    Number of cleanable squares.
  """
  pass

if __name__ == "__main__":
  grid = [
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
    ".....................................................................",
  ]
  assert cleanable_squares_number(grid) == len(grid) * 2 + (len(grid[0]) - 2) * 2
    
