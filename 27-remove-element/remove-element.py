class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        for _ in range(len(nums)):
            nums.remove(val) if val in nums else None
        return  len(nums)