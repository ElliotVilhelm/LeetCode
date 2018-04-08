# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        q1 = [p]
        q2 = [q]
        while (len(q1) > 0 and len(q2) > 0):
            v1 = q1.pop()
            v2 = q2.pop()
            # print(v1.val, v2.val)
            if (v1 is None and v2 is None):
                continue
            elif (not v1 or not v2):
                return False
            elif (v1 and v2 and v1.val != v2.val):
                return False
            if (v1.left and v2.left):
                q1.append(v1.left)
                q2.append(v2.left)
            elif(v1.left or v2.left):
                return False
            if (v1.right and v2.right):
                q1.append(v1.right)
                q2.append(v2.right)
            elif (v1.right or v2.right):
                return False

        if (len(q1) != 0 or len(q2) != 0):
            return False

        return True
