from leetcode.add_binary import add_binary


def test_example_1():
    answer = add_binary("11", "1")
    assert answer == "100"


def test_example_2():
    answer = add_binary("1010", "1011")
    assert answer == "10101"


def test_example_3():
    answer = add_binary("1010", "0101")
    assert answer == "1111"


def test_example_4():
    answer = add_binary("1010", "0100")
    assert answer == "1110"


def test_example_5():
    answer = add_binary("11", "")
    assert answer == "11"


def test_example_6():
    answer = add_binary("1111", "1111")
    assert answer == "11110"
