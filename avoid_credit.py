from typing import List

def minimum_relocations(A: List[int]) -> int:
    expanses = {
        str(index_expanse): value_expanse
        for index_expanse, value_expanse in enumerate(A)
        if value_expanse < 0
    }
    relocations_number = 0
    index = 0
    while index < len(A):
        if sum(A[: index + 1]) < 0 and any(value > 0 for value in A[index + 1 :]):
            A.append(
                A.pop(
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
