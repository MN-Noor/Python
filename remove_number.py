nums = [0,1,2,2,3,0,4,2]
val = 2
class Solution(object):
    def removeElement(self, nums, val):
        i, k = 0, len(nums)
        while i < k:
                if nums[i] == val:
                    k-=1
                    nums[i] = nums[k]
                else:
                    i += 1

        return k