# Minimum Difference Between Largest and Smallest Value in Three Moves
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums.sort()
        res=float("inf")
        for i in range(4):
            r=len(nums)-4+i
            res=min(res,nums[r]-nums[i])
        return int(res)
        