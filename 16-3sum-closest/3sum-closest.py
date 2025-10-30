class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i , num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if abs(threeSum - target) < abs(result - target):
                    result = threeSum
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    return threeSum
        return result