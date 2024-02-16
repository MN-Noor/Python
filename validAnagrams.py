class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count={}
        for char1,char2 in  zip(s,t):
            count[char1]=count.get(char1,0)+1
            count[char2]=count.get(char2,0)-1

        for char in t:
            if count[char]!=0:
                return False
        return True
           

