class Solution(object):
    def minWindow(self, s, t):
        if t=="":  return  ""
        swindow={}
        tcount={}
        i=0
        res=[-1,-1]
        resLength=float("infinity")
        for c in t:
            tcount[c]=1+tcount.get(c,0)

        have,need=0,len(tcount)

        for j  in range(len(s)):
            c=s[j]
            if c in tcount: 
                swindow[c]=1+swindow.get(c,0)
                if  swindow[c]==tcount[c]:
                    have+=1

            while have==need:
                if j-i+1<resLength:
                    resLength=j-i+1
                    res=[i,j]
                
                if s[i] in tcount:
                    swindow[s[i]]-=1
                    if swindow[s[i]]<tcount[s[i]]:
                        have-=1
                i+=1
        l,r=res[0],res[1]
        return  s[l:r+1] if resLength!=float("infinity") else  ""


       