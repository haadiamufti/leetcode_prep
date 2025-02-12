# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. 
# The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_min_value(root, mini = float("inf")):
  if root is None:
    return mini
  if root.val < mini:
    mini = root.val
  left = tree_min_value(root.left, mini) 
  right = tree_min_value(root.right, mini)
  return min(left, right)
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
print(tree_min_value(a)) # -> -2
