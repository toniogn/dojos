from typing import List

def minimum_relocations(operations: List[int]) -> int:
    """Determines the minimum negative values relocation number to the end of a list to ensure positive accumulation.
    
    Parameters
    ----------
    operations : List[int]
        Chronological list of operations.
    
    Returns
    -------
    relocations_number : int
        Minimum number of expanses to relocate.
    """
    relocations_number = 0
    index = 0
    while index < len(operations):
        if sum(operations[: index + 1]) < 0 and any(value > 0 for value in operations[index + 1 :]):
            relocate(operations, index)
            relocations_number += 1
        else:
            index += 1
    return relocations_number

def relocate(operations: List[int], index: int) -> None:
    """Relocate the biggest expanse at the end of the operations list.
    
    Parameters
    ----------
    operations : List[int]
        Chronological list of operations.
    index : int
        Current index where the accumulated operations leads to a negative amount.
    """
    operations.append(
        operations.pop(
            min(
                range(index + 1),
                key=lambda i: operations[i],
            )
        )
    )
