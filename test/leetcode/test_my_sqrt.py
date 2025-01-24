import math

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


def test_example_5():
    answer = my_sqrt(9)
    assert answer == 3


def test_example_6():
    answer = my_sqrt(25)
    assert answer == 5


def test_example_7():
    answer = my_sqrt(6)
    assert answer == 2


def test_all():
    for i in range(30):
        assert math.floor(math.sqrt(i)) == my_sqrt(i)
