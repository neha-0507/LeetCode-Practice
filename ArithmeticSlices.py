# Time Complexity - O(N^2)
# Space Complexity - O(1)

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if(A==0 or len(A)<3):
            return 0
        count = 0
        for i in range(0,len(A)-2):
            diff = A[i1] - A[i]
            for j in range(i+2,len(A)):
                if((A[j]-A[j-1])==diff):
                    count+=1
                else:
                    break
        return count
    
# Time Complexity - O(N)
# Space Complexity - O(N)

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if(A==0 or len(A)<3):
            return 0
        sum = 0
        n = len(A)
        dp=[0]*n
        for i in range(len(dp)-3,-1,-1):
            if((A[i+1]-A[i])==(A[i+2]-A[i+1])):
                dp[i]=dp[i+1] + 1
                sum+=dp[i]
        return sum
        
  # Time Complexity - O(N)
  # Space Complexity - O(1)
  
  class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if(A==0 or len(A)<3):
            return 0
        sum = 0
        curr, right = 0, 0
        for i in range(len(A)-3,-1,-1):
            if((A[i+1]-A[i])==(A[i+2]-A[i+1])):
                curr = right + 1
                sum+= curr
                right = curr
                print(curr,right)
                
            else:
                right = 0
        return sum
