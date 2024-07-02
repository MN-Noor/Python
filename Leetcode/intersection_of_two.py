class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map={}
        for value in nums1:
            map[value]=map.get(value,0)+1
        nums1.clear()
        for value in nums2:
            if value in map:
                if map[value]>0:
                    map[value]=map.get(value,0)-1
                    nums1.append(value)
        return nums1
    
# Time Complexity: O(n+m)
#space complexity: O(n)

# using python sort for intersection
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       i,j=0,0
       res=[]
       nums1.sort()
       nums2.sort()
       while i<len(nums1) and  j<len(nums2):
        if nums1[i]==nums2[j]: 
            res.append(nums1[i])
            i+=1
            j+=1
        else:
            if nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
       return(res)

#time complexity=O(2nlog(n)+n)=O(nlog(n))
#space complexity=O(n)
