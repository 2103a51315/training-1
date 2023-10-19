# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(si,ei):
            if si<=ei:
                mid=(si+ei)//2
                root=TreeNode(nums[mid])
                root.left=bst(si,mid-1)
                root.right=bst(mid+1,ei)
                return root
        return bst(0,len(nums)-1)
#  convert sorted array inti binary search tree           
            
            
                
            

        

        