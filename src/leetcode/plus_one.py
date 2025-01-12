def plus_one(data: list):
    carry = False

    for i in range(len(data) - 1, -1, -1):
        if carry and data[i] < 9:
            data[i] = data[i] + 1
            return data

        if data[i] < 9:
            data[i] = data[i] + 1
            return data
        else:
            data[i] = 0
            carry = True

    if carry:
        data.insert(0, 1)

    return data
