class Solution(object):
    def twoSum(self, nums, target):
        diff={}
        for  i,num in enumerate(nums):
            compliment=target-num
            if compliment in diff:
                return [diff[compliment],i]
            else:
                diff[num]=i
        return None
