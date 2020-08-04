# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ans = 1
        rec = float('-inf')
        stp = 0
        stk = [root]
        while stk:
            tmp = 0
            stp += 1
            tstk = []
            for i in stk:
                tmp += i.val
                if i.left:
                    tstk.append(i.left)
                if i.right:
                    tstk.append(i.right)
            if tmp > rec:
                rec = tmp
                ans = stp
            stk = tstk
        return ans
