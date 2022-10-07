class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        runningTotal = 0
        result = []
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num + num2 == target:
                    result.append(i)
                    result.append(j)
        return result