from leetcode.two_sum import two_sum


def test_example_1():
    answer = two_sum([2, 7, 11, 15], 9)
    assert answer == [0, 1]


def test_no_solution():
    """Test the edge case where no solution is found (should not happen in practice)."""
    answer = two_sum([], 1)  # Empty array, no solution possible
    assert answer == []
