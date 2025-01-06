from leetcode.length_of_last_word import length_of_last_word


def test_example_1():
    answer = length_of_last_word("Hello World")
    assert answer == 5


def test_example_2():
    answer = length_of_last_word("Hello World  ")
    assert answer == 5


def test_example_3():
    answer = length_of_last_word("   ")
    assert answer == 0
