def length_of_last_word(s: str) -> int:
    answer = 0

    for c in s[::-1]:

        if c == " " and answer == 0:
            continue

        if c == " ":
            return answer

        answer += 1

    return answer
