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
    relocations_number = 0
    index = 0
    while index < len(operations):
        if sum(operations[:index + 1]) < 0:
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
