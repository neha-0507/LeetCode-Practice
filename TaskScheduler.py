# Time Complexity - O(N)
# Space Complexity - O(1)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if(tasks==None or len(tasks)==0):
            return 0
        maxFreq, maxCount = 0,0
        dict={}
        for i in tasks:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        maxFreq=max(dict.values())
        for values in dict.values():
            if(values==maxFreq):
                maxCount+=1
        partition=(maxFreq-1)
        empty=(n-(maxCount-1))*partition
        pendingElement=len(tasks)-(maxFreq*maxCount)
        idle=max(0,empty-pendingElement)
        res=len(tasks)+idle
        return res
