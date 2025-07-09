from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of two numbers.
    The indices should be of numbers that add up to the target value.
    """
    # Create a hash map to store numbers and their indices
    num_map = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # If the complement is in the map, we found our solution
        if complement in num_map:
            return [num_map[complement], i]

        # Otherwise, add the current number and its index to the map
        num_map[num] = i

    # If no solution is found (should not happen based on problem constraints)
    return []
