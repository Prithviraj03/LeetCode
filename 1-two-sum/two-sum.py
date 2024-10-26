from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            # Check if the complement is already in the dictionary
            if complement in seen:
                return [seen[complement], i]
            # Store the index of the current number
            seen[num] = i
