class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for strings in strs:
            res+=str(len(strings))+"#"+strings
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            strln=int(s[i:j])
            res.append(s[j+1:j+1+strln])
            i=j+1+strln
        return res