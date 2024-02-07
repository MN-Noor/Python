#using hashmap/dict
class Solution(object):
    def majorityElement(self, nums):
        hash={}
        n=len(nums)/2
        num,count=0,0
        for num in nums:
            hash[num]=1+hash.get(num,0)
            if hash[num]>n:return num
        
        return -1
#using boyer moore vooting algorithm
    class Solution(object):
        def majorityElement(self, nums):
            candidate=0
            count=0
            for num in nums:
                if count==0:
                    candidate=num
                if candidate==num:
                    count+=1
                else:
                    count-=1
            return candidate