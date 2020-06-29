# Time Complexity - O(N)
# Space Complexity - O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(nums==None or len(nums)==0):
            return True
        destination=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(i+nums[i]>=destination):
                destination=i
        if(destination!=0):
            return False
        return True
