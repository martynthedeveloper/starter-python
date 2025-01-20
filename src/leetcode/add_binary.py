# https://leetcode.com/problems/add-binary/description/


def add_binary(a: str, b: str) -> str:
    size = max(len(a), len(b))
    answer = ""
    carry = 0

    for i in range(size):
        aa = 0 if i >= len(a) else int(a[len(a) - i - 1])
        bb = 0 if i >= len(b) else int(b[len(b) - i - 1])

        ia = aa + bb + carry

        if ia == 0:
            answer = "0" + answer
            carry = 0
        elif ia == 1:
            answer = "1" + answer
            carry = 0
        elif ia == 2:
            answer = "0" + answer
            carry = 1
        else:  # ia == 3
            answer = "1" + answer
            carry = 1

    if carry:
        answer = "1" + answer

    return answer
