class Solution(object):
    def twoSum(self, nums, target):      # nums: List[int], target: int, o/p: List[int]
        if len(nums) <=1:
            return False
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return dict[nums[i]], i
            else:
                dict[target-nums[i]] = i

s= Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums,target))
