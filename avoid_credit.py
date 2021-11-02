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
    expanses = {
        str(index_expanse): value_expanse
        for index_expanse, value_expanse in enumerate(operations)
        if value_expanse < 0
    }
    relocations_number = 0
    index = 0
    while index < len(operations):
        if sum(operations[: index + 1]) < 0 and any(value > 0 for value in operations[index + 1 :]):
            operations.append(
                operations.pop(
                    min(
                        (
                            int(index_expanse)
                            for index_expanse in expanses.keys()
                            if int(index_expanse) <= index
                        ),
                        key=lambda index_expanse: expanses[str(index_expanse)],
                    )
                )
            )
            relocations_number += 1
        else:
            index += 1
    return relocations_number
