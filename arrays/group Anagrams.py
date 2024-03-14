class Solution(object):
    def groupAnagrams(self, strs):
        res=[]
        if len(strs)<=1:
            res.append(strs)
            return res

        hash={}
       
        index=0
        for word in strs:
            
            sortw="".join(sorted(word))
            if sortw in hash:
                res[hash[sortw]].append(word)
            else:
                hash[sortw]=index
                index+=1
                res.append([word])
        return res

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        