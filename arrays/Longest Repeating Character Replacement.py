class Solution(object):
    def characterReplacement(self, s, k):
        count={}
        l=0
        res=0
        maxfreq=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxfreq=max(maxfreq,count[s[r]])
            if (r-l+1)-maxfreq>k:
                count[s[l]]=count.get(s[l],0)-1
                l+=1
            else:
                res=max(res,r-l+1)

            
        return res
                
