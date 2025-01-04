class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i in range(len(nums)):
            if str(nums[i]) in dict:
                return [ dict[str(nums[i])], i ]
            
            dict[str(target - nums[i])] = i
