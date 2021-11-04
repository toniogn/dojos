def previous_steps_number(step_index: int) -> int:
    """Counts the number of steps leading to the one identified by its index.

    Parameters
    ----------
    step_index : int
        Index of the current step.

    Returns
    -------
    int
        Number of steps from which one can reach the current one.
    """
    if step_index >= 1:
        return previous_steps_number(step_index - 1) + previous_steps_number(
            step_index - 2
        )
    elif step_index == 0:
        return 1
    elif step_index < 0:
        return 0
 

def stair_path_number(stair_steps_number: int) -> int:
    """Counts the number of different path to climb the stairway depending on its steps number.
    
    Parameters
    ----------
    stair_steps_number : int
        Number of steps of the stair.

    Returns
    -------
    int
        Number of different path to climb the stairway.
    """
    return previous_steps_number(stair_steps_number)
