# https://leetcode.com/problems/plus-one/
from leetcode.plus_one import plus_one


def test_example_1():
    answer = plus_one([1, 2, 3])
    assert answer == [1, 2, 4]


def test_example_2():
    answer = plus_one([4, 3, 2, 1])
    assert answer == [4, 3, 2, 2]


def test_example_3():
    answer = plus_one([9])
    assert answer == [1, 0]


def test_example_4():
    answer = plus_one([1, 9])
    assert answer == [2, 0]


def test_example_5():
    answer = plus_one([1, 2, 9])
    assert answer == [1, 3, 0]
