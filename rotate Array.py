class Solution(object):
    def rotate(self, nums, k):
        list=nums[:]
        size=len(nums)
        for  i in range(size):
            j=(i+k)%size
            nums[j]=list[i]
        
    #in O(1)time complexity
class Solution(object):
    def rotate(self, nums, k):
       
        size=len(nums)
        k=k%size
        self.reverseArray(0,size-1,nums)
        self.reverseArray(0,k-1,nums)
        self.reverseArray(k,size-1,nums)

        
    def reverseArray(self,l,r,list):
        while  l<r:
            list[l],list[r]=list[r],list[l]
            l+=1
            r-=1
       
        
            