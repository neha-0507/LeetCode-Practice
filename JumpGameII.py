# Time Complexity- O(N)
# Space Complxity - O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        if(nums==None or len(nums)<2):
            return 0
        jump=1
        curr_number=nums[0]
        next_number=nums[0]
        for i in range(1,len(nums)):
            next_number=max(next_number, i+nums[i])
            if(i<len(nums)-1 and curr_number==i):
                curr_number=next_number
                jump+=1
        return jump
