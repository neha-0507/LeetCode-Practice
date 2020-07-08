# Time Complexity - O(N)
# Space Complexity - O(1)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result=[]
        if(S==None or len(S)==0):
            return result
        lastOccuring={}
        for i in range(len(S)):
            lastOccuring[S[i]]=i
        start, end = 0, 0
        for i in range(len(S)):
            end=max(end,lastOccuring[S[i]])
            if(end==i):
                result.append(end-start+1)
                start=end+1
        return result
        
