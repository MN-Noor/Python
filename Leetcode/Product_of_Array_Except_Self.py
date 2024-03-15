class Solution(object):
    def productExceptSelf(self, nums):
        size=len(nums)
        l=[1]*size
        result=[1]*size
        right=1
        left=1
        for i in range (size):
            l[i]=left
            left=left*nums[i]

        for i in reversed(range(size)):
            result[i]=right*l[i]
            right=right*nums[i]
        return result
    #2nd Time

class Solution(object):
    def productExceptSelf(self, nums):
        pos,pre=1,1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*pos
            pos*=nums[i]
        return res

        
        