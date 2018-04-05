# Python program to do inorder traversal without recursion
# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None


"""
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL

4) If current is NULL and stack is not empty then
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right
     c) Go to step 3
5) If current is NULL and stack is empty then we are done.
"""
# Driver program to test above function


def swap_nodes(root):
    s = []  # 1) create an empty stack
    current_node = root  # 2) initialize current node as root
    while (current_node != None):

        # 3)
        s.append(current_node)  # Push the current node to S
        current_node = current_node.left  # set current = current->left until current is NULL






""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """

 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
