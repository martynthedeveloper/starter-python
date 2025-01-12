from typing import List


def plus_one(digits: List[int]) -> List[int]:
    carry = False

    for i in range(len(digits) - 1, -1, -1):
        if carry and digits[i] < 9:
            digits[i] = digits[i] + 1
            return digits

        if digits[i] < 9:
            digits[i] = digits[i] + 1
            return digits

        digits[i] = 0
        carry = True

    if carry:
        digits.insert(0, 1)

    return digits
