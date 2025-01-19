from leetcode.my_sqrt import my_sqrt


def test_example_1():
    answer = my_sqrt(4)
    assert answer == 2


def test_example_2():
    answer = my_sqrt(8)
    assert answer == 2


def test_example_3():
    answer = my_sqrt(0)
    assert answer == 0


def test_example_4():
    answer = my_sqrt(1)
    assert answer == 1
