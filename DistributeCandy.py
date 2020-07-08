# Time Complexity - O(N)
# Space Complexity - O(N)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if(ratings==None or len(ratings)==0):
            return 0
        n=len(ratings)
        candies=[1]*n
        # LEFT PASS
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                candies[i]=candies[i-1]+1
        # RIGHT PASS
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i]>ratings[i+1]):
                candies[i]=max(candies[i],candies[i+1]+1)
        sum=0
        for i in candies:
            sum=sum+i
        return sum
        
