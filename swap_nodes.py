"""
Swap Nodes
"""

# Tree Node Class
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def swap_nodes(root):
    nodes_in_dfs = []
    if root is None:
        return
    # s emulates the run time stack
    s = []  # 1) create an empty stack
    current_node = root  # initialize current node as root
    while True:
        while current_node is not None:
            s.append(current_node)  # Push the current node to s
            current_node = current_node.left  # set current = current->left until current is NULL
        node = s.pop()
        print(node.data)
        nodes_in_dfs.append(node)
        current_node = node.right
        if current_node is None and len(s) is 0:
            break

    swap_me = find_swaps(nodes_in_dfs)
    if len(swap_me) < 2 or len(swap_me) > 3:
        return
    else:  # swap
        if len(swap_me) == 2:
            save_val = nodes_in_dfs[swap_me[0]].data
            nodes_in_dfs[swap_me[0]].data = nodes_in_dfs[swap_me[1]].data
            nodes_in_dfs[swap_me[1]].data = save_val
        else:
            save_val = nodes_in_dfs[swap_me[0]].data
            nodes_in_dfs[swap_me[0]].data = nodes_in_dfs[swap_me[2]].data
            nodes_in_dfs[swap_me[2]].data = save_val


def find_swaps(l):
    """
    :param l: list of nodes in dfs order
    :return:  list of index of nodes to be swapped
    """
    swaps = []
    for i in range(len(l)-1):
        if l[i+1].data < l[i].data:
            if len(swaps) == 0:
                swaps.append(i)
                swaps.append(i+1)
            else:
                swaps.append(i+1)


    return swaps


""" Constructed binary tree is
            5
          /   \
         3     6
       /  \
      1    4   """


root = Node(5)
root.left = Node(6)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(4)

swap_nodes(root)
swap_nodes(root)
