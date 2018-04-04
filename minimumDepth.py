# Definition for a binary tree node.
class TreeNode:
        def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(4)


# root is a node object
def minDepth(root):
        # visit root
        # visit left
        # if left is a leaf then return n nodes visited
        # else add it to list to visit
        # visit right
        # if right is leaf ..
        # else add it to list to visit
        if root is None:
                return 0
        q = [(root, 1)]

        count = 1
        while (len(q) > 0):
                v, count = q.pop()
                print("v :", v.val)
                if v.left is None and v.right is None:
                        return count
                if v.left is not None:
                        q.insert(0, (v.left, count+1))
                if v.right is not None:
                        q.insert(0, (v.right, count+1))
                count += 1



foundmin = minDepth(root)
print(foundmin)
