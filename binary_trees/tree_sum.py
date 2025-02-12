# Write a function, tree_sum, that takes in the root of a binary tree that contains number values.
# The function should return the total sum of all values in the tree.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_sum(root):
  if root is None:
    return 0
    
  return root.val + tree_sum(root.right) + tree_sum(root.left)

      
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

print(tree_sum(a)) # -> 10

