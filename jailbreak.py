"""
Homework 04 - JailBreak

Student: Kelsey Edinborough
Semester: Fall 2024

This assignment focuses on learning while loops. It
is inspired by

Think Like a Coder ep1 Lesson by Alex Rosenthal, directed by Kozmonot Animation Studio.

https://www.youtube.com/watch?v=KFVdHDMcepw&list=PLJicmE8fK0EgogMqDYMgcADT1j5b911or&index=2
"""
from random import randint
from lock_tools import COMBO, PATTERN, MAX_PATTERN_SIZE, check_solution, is_open, \
    get_lock_type, new_door, get_single_combo, get_single_pattern
# by importing these functions and variables, you can use them directly in your code
# for example:
#  if get_lock_type(val) == COMBO:
#      do something
# get_single_combo(), and get_single_pattern() will help with interactive testing (see readme)


def unlock_combo_lock(lock_id: int) -> int:
    """
    Checks possible combinations for a combo lock, until
    the correct solution is found.

    Args:
        lock_id (int): the lock to check

    Returns:
        (int): the solution to the lock, or minus 1 if not found
    """
    i = 0
    while not check_solution(lock_id, i):
        i += 1

    return i


# you may find it easier to add another function to build the pattern first..

def pattern_x_bottom(size: int = 13, space: str = ' ', fill: str = 'x') -> str:
    """ Going to make the bottom part of the x pattern
        Args:
            size(int): the size of the X pattern
            space(str): the string that will fill the spaces around the X pattern
            fill(str): the string that will create the X pattern 
        Returns: 
            str: the bottom part of the X pattern 


    """
    x = ''
    lines = 0
    fill_count = 0
    remove = 1
    yo = int((size - 1) / 2)
    while lines <= size:
        if (lines % 2 == 1) and (lines == 1):
            x += space + (space * (yo - remove)) + (fill * fill_count) + \
                (space * (yo - remove)) + (space) + "\n"
        if (lines % 2 == 1) and (lines > 1):
            x += (space * (yo - remove)) + (fill) + (space *
                                                     (fill_count - 2)) + (fill) + (space * (yo - remove)) + "\n"
            remove += 1
        fill_count += 1
        lines += 1

    return x


def pattern_x_top(size: int = 13, space: str = ' ', fill: str = 'x') -> str:
    """ Going to make the top part of the x pattern

        Args:
            size(int): the size of the X pattern
            space(str): the string that will fill the spaces around the X pattern
            fill(str): the string that will create the X pattern

        Returns: 
            str: the top part of the X pattern 


    """

    x = ''

    fill_count = 0
    yo = int((size - 1) / 2)
    remove = yo
    lines = size
    while lines > 1:
        if (lines % 2 == 1):
            x += (space * (yo - remove)) + (fill) + (space * (lines - 2)
                                                     ) + (fill) + (space * (yo - remove)) + "\n"
            remove -= 1
        lines -= 1

    return x


def pattern_x_final(size: int = 13, space: str = ' ', fill: str = 'x') -> str:
    """Combining top and bottom of X to make the final X pattern 
        Args:
            size(int): the size of the X pattern
            space(str): the string that will fill the spaces around the X pattern
            fill(str): the string that will create the X pattern 
        Returns: 
            str: the  X pattern 

    """
    final = pattern_x_top(size, space, fill) + \
        pattern_x_bottom(size, space, fill)
    return final


def unlock_pattern_lock(lock_id: int) -> str:
    """
    Checks possible patterns for a pattern lock, until
    the correct solution is found.

    Args:
        lock_id (int): the lock to check

    Returns:
        str: The pattern solution to the lock
    """

    zero_pattern = pattern_x_final(0)
    if check_solution(lock_id, zero_pattern):
        return zero_pattern

    i = 1
    pattern = pattern_x_final(1)
    while not check_solution(lock_id, pattern):
        i += 2
        pattern = pattern_x_final(i)

    return pattern


def open_door(num_locks: int) -> bool:
    """
    Opens a door with a number of locks. The door is opened by
    guessing the correct solution to each lock.

    Args:
        num_locks (int): the number of locks on the door

    Returns:
        bool: True if the door is opened, False otherwise
    """
    counter = 0
    while counter < num_locks:
        lock_type = get_lock_type(counter)

        if lock_type == COMBO:
            unlock_combo_lock(counter)
            return counter + 1

        if lock_type == PATTERN:
            unlock_pattern_lock(counter)
            return counter + 1

    # Optional - you  may find it useful adding this, your variable names may differ
    # print(__FEEDBACK_MESSAGE.format(lock_type=lock_type, lock_id=lock_id, solution=final))
    return is_open()


def main():
    """ Starting point for the program. """
    print(__WELCOME_MESSAGE)
    total_doors = randint(1, 6)  # generate a random number of doors
    counter = 0
    while counter < total_doors:
        locks = new_door()
        print(__OPENING_DOOR_MESSAGE.format(counter=counter + 1, locks=locks))
        if not open_door(locks):
            print(__TRAPPED_MESSAGE)
            return
        counter += 1
    print(__GOODBYE_MESSAGE)


__WELCOME_MESSAGE = """Hello explorer! You have been captured and placed in a jail cell.
The only way to escape is to open the door. Make use of your infobot to help you escape."""
__GOODBYE_MESSAGE = "Congratulations! You have escaped the jail cell. You are now free."
__OPENING_DOOR_MESSAGE = "Opening door number: {counter} with {locks} locks."
__TRAPPED_MESSAGE = "You have been trapped. Better luck next time. (check for errors in your code)"
__FEEDBACK_MESSAGE = "Opened lock {lock_type} {lock_id} with solution\n{solution}"


if __name__ == "__main__":
    main()
