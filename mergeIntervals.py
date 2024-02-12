class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res=[]
        res.append(intervals[0])
        size=len(intervals)
        for i in range(1,size):
            lindex=len(res)-1
            if res[lindex][1]>=intervals[i][0]:
                lrange=min(res[lindex][0],intervals[i][0])
                mrange=max(res[lindex][1],intervals[i][1])
                res[lindex]=[lrange,mrange]
            else:
                res.append(intervals[i])

        return res