# https://leetcode.com/problems/sqrtx/description/


def my_sqrt(x: int) -> int:
    """
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.
    """
    if x in (0, 1):
        return x

    # Use binary search to find the square root
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2

        # If mid*mid is equal to x, we found the exact square root
        if mid * mid == x:
            return mid

        # If mid*mid is greater than x, search in the left half
        if mid * mid > x:
            right = mid - 1
        # If mid*mid is less than x, search in the right half
        else:
            left = mid + 1

    # When we exit the loop, right is the integer part of the square root
    return right
