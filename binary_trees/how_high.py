# Write a function, how_high, that takes in the root of a binary tree. 
# The function should return a number representing the height of the tree.

# The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

# If the tree is empty, return -1.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def how_high(node):
  if node is None:
    return -1
  elif node.right is None and node.left is None:
    return 0
  elif node.right is not None or node.left is not None:
    return 1 +  max(how_high(node.right), how_high(node.left))
  
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(how_high(a)) # -> 3


