# https://leetcode.com/problems/sqrtx/description/


def my_sqrt(x: int) -> int:
    if x == 1:
        return 1

    left = 0
    right = int(x / 2)
    guess = 0

    while right - left >= 1:
        guess = left + int((right - left) / 2)
        square = guess * guess

        if square == x:
            return guess

        if square < x:
            left = guess + 1
            guess = guess + 1
        else:
            right = guess - 1
            guess = guess - 1

    return guess


# . sqrt(8)
# . 0 1 2 3 4
# . l   g   r s=4
# .     l g r s=9
# .     l r   s=
# .
# .
# .
