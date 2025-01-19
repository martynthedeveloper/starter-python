def my_sqrt(x: int) -> int:
    if x == 1:
        return 1

    answer = 0
    for i in range(x):
        if i * i <= x:
            answer = i
        else:
            break

    return answer
