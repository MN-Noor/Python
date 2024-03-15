class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        longestseq=0
        for num in nums:
            if (num-1) not in s:
                length=0
                while (num+length) in s:
                    length+=1
                longestseq=max(longestseq,length)
        return longestseq