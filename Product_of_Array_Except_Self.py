lass Solution(object):
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
