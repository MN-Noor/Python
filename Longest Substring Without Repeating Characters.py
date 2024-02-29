class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l,r=0,0
        check=set()
        res=0
        while r<len(s):
            if s[r] not in check:
                check.add(s[r])
                r+=1
                res=max(res,r-l)
            else:
                check.remove(s[l])
                l+=1

        return res
# //second
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        check=set()
        res=0
        for r in range(len(s)):
           while s[r] in check:
               check.remove(s[l])
               l+=1
           check.add(s[r])
           res=max(res,r-l+1)
        return res