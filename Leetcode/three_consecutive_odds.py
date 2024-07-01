class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddcount=0
        for value in arr:
            if value%2!=0:
                oddcount=oddcount+1
                if oddcount>=3:
                    return  True
            else:
                oddcount=0
        
        else:
            return False

        