from leetcode.add_binary import add_binary


def test_example_1():
    answer = add_binary("11", "1")
    assert answer == "100"


def test_example_2():
    answer = add_binary("1010", "1011")
    assert answer == "10101"
