# #brute force
class Solution(object):
    def threeSum(self, nums):
   
        rs=[]
        size=len(nums)
        for i in range(size-2):
            for j in range(i+1,size-1):
                for k  in range (j+1,size):
                    if nums[i]+nums[j]+nums[k]==0:
                        ls=[nums[i],nums[j],nums[k]]
                        ls.sort()
                        if  ls  not in rs:
                            rs.append(ls)
        return rs
#with HashTable Technique
class Solution(object):
    def threeSum(self, nums):
        hash={}
        res=[]
        size=len(nums)
        i,j=0,0
        for i in range(i,size):
            for j in range(i+1,size):
                target=-(nums[i]+nums[j])
                if target in hash:
                    trip=[nums[i],nums[j],target]
                    trip.sort()
                    if trip not in res:
                        res.append(trip)

                else:
                    hash[nums[j]]=j
            hash.clear()
        return res
#with two pointer
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res=set()
        size=len(nums)
        for i in range(size-2):
            l=i+1
            r=size-1
            while l<r:
                target=nums[i]+nums[l]+nums[r]
                if  target==0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                    
                elif target<0:
                    l+=1
                    
                else:
                    r-=1
                    
            
        return res


        
