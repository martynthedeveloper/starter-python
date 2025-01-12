def plus_one(data: list):

    for i in range(len(data) - 1, -1, -1):
        print(data[i])
        if data[i] < 9:
            data[i] = data[i] + 1
            return data

        data[i] = 0
        data.insert(i, 1)

    return data
