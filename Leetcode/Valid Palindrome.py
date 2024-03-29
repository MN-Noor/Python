class Solution(object):
    def isPalindrome(self, s):
        i,j=0,len(s)-1
        while i<j:
            while i<j and not self.isalnum(s[i]):
               i+=1
            while j>i and not self.isalnum(s[j]):
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
            

    def isalnum(self,c):
        return(ord('A')<=ord(c)<=ord('Z')or
        ord('a')<=ord(c)<=ord('z')or
        ord('0')<=ord(c)<=ord('1'))
