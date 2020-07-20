# Time Complexity - O(nlog(Whigh - Wlow)
# Space Complexity - O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if(weights== None or len(weights)==0):
            return 0
        low = 0
        high = 0
        for w in weights:
            low= max(low,w)
            high+=w
        while(low<=high):
            mid = low+((high-low)//2)
            currDay = 1
            currSum = 0
            for i in range(0,len(weights)):
                if(currSum+weights[i] > mid):
                    currDay+=1
                    currSum=0
                currSum+=weights[i]
                
            if(currDay> D):
                low = mid+1
            else:
                high = mid-1
        return low
