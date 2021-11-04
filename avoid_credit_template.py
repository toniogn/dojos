import numpy as np
from typing import List


def minimum_relocations(operations: List[int]) -> int:
  """Count the minimum expanses relocations number from a chronological operations list.
  
  Parameters
  ----------
  operations : List[int]
    List of operations (negative expanses and positive incomes) that sums up to a positive or zero value.
    
  Returns
  -------
  int
    Minimum number of expanses relocations to the end of the operations list to realize to ensure positivity of every accumulated sums.
  """
  pass


def operations_generator(operations_number: int) -> List[int]:
  """Generate an operations list according to operations number.
  
  Parameters
  ----------
  operations_number : int
    Operations number.
    
  Returns
  -------
  List[int]
    List of operations that sums up to zero.
  """
  assert operations_number % 2 != 0
  return (round(value) for value in 100 * np.cos([k * 2 * np.pi/(operations_number - 1) for k in range(operations_number)]))


if __name__ == "__main__":
    for operations_number, minimum_relocations_number in [(int(1e3 + 1), 167)]:
      assert minimum_relocations(list(operations_generator(operations_number))) == minimum_relocations_number

