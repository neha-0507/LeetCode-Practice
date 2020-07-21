# Time Complexity - O(N)
# Space Complexity - O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        self.dfs(root)
        return self.moves
    
    def dfs(self,root):
        #Base
        if(root==None):
            return 0
        #logic
        leftCoins = root.val -1
        leftCoins+= self.dfs(root.left)
        leftCoins+= self.dfs(root.right)
        self.moves+= abs(leftCoins)
        return leftCoins
