# Time complexity --> o(k**(n/k)) where k is the number of blocks and n is the total number of elements
# space complexity --> o(product of the number of elements in each block)
class Solution:
    def __init__(self):
        self.result = []
    def expand(self, S: str) -> List[str]:
        block = []
        if(S==None or len(S)==0):
            return []
        # To append into block of array
        #{a b c}d{e f} = [[a,b,c][d][e,f]]
        i =0
        while i<len(S):
            val=[]
            if S[i]=='{':
                while(S[i]!='}'):
                    if(S[i]!=',') and (S[i]!='{'):
                        val.append(S[i])
                    i+=1
            else:
                val=[S[i]]
            block.append(val)
            i+=1
        self.dfs(block,0,'')
        self.result.sort()
        return self.result
            
    def dfs(self,block,index,str1):
        #Base Case
        if(index == len(block)):
            self.result.append(str1)
            return
        # Logic
        value1 = block[index]
        for i in value1:
            # Add char to string
            str1 = str1 + i
            # Backtrack
            self.dfs(block, index+1 , str1)
            # Delete the element
            str1 = str1[:-1]
