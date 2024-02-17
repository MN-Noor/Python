class Solution(object):
    def topKFrequent(self, nums, k):
        count={}
        bucket=[[]for _ in range(len(nums)+1)]
        for i in  nums:
            count[i]=count.get(i,0)+1
        for key,value in count.items():
            bucket[value].append(key)
            res=[]
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                
                res.append(j)
                if(len(res)==k):
                    return res
