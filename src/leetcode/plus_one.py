from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    Given a non-empty array of decimal digits representing a non-negative integer,
    increment one to the integer.

    The digits are stored such that the most significant digit is at the head of the list.
    """
    n = len(digits)

    # Start from the last digit and move towards the first
    for i in range(n - 1, -1, -1):
        # If the current digit is less than 9, simply increment it and return
        if digits[i] < 9:
            digits[i] += 1
            return digits

        # If the current digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0

    # If we're here, it means all digits were 9, so we need to add a 1 at the beginning
    return [1] + digits
