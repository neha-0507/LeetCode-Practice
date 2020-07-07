# Time Complexity - O(2^N)
# Space Complexity - O(N) 
class Solution:
                        
    def isValid(self,s):
        count=0
        for i in range(len(s)):
            if(s[i]=='('):
                count+=1
            elif(s[i]==')'):
                count-=1
            if(count<0):
                return False
        return (count==0)
                
    def removeInvalidParentheses(self, s: str) -> List[str]:
        finalResult = []
        if(s==None):
            return finalResult
        levelStrings = set()

        queue = []
        queue.append(s)
        while(queue):
            levelCount = len(queue)
            for i in range(levelCount):
                currentString = queue.pop(0)
                if (currentString not in levelStrings):
                    if (self.isValid(currentString)):
                        finalResult.append(currentString)
                    else:
                        if (len(finalResult) <= 0):
                            for j in range(len(currentString)):
                                if (currentString[j] == '(' or currentString[j] == ')'):
                                    child = currentString[: j] + currentString[j+1: ]
                                    queue.append(child)
               
                levelStrings.add(currentString)                   
            levelStrings = set()
                      
        return finalResult
