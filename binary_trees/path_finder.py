# Write a function, path_finder, that takes in the root of a binary tree and a target value. 
# The function should return an array representing a path to the target value. If the target value is not
# found in the tree, then return None.

# You may assume that the tree contains unique values.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [root.val]
  right = path_finder(root.right, target)
  left = path_finder(root.left, target)
  if right is None and left is None:
    return None 
  if right is None:
    return  [root.val] + left
  elif left is None:
    return [root.val] + right
  
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]
