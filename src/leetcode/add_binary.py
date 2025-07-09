# https://leetcode.com/problems/add-binary/description/


def add_binary(a: str, b: str) -> str:
    """
    Given two binary strings a and b, return their sum as a binary string.
    """
    result = ""
    carry = 0

    # Make sure both strings have the same length by padding with zeros
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(a), len(b)))

    # Iterate from right to left
    for i in range(len(a) - 1, -1, -1):
        # Convert characters to integers and add them with the carry
        digit_sum = int(a[i]) + int(b[i]) + carry

        # Calculate the new digit and carry
        result = str(digit_sum % 2) + result
        carry = digit_sum // 2

    # If there's a carry left, add it to the beginning
    if carry:
        result = "1" + result

    return result
