# Write a function, depth_first_values, that takes in the root of a binary tree. 
# The function should return a list containing all values of the tree in depth-first order.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_values(root):
  stack = [root]
  values = []
  if root is None:
    return []
  while stack != []:
    current = stack.pop()
    values.append(current.val)
    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)
  return values

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
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

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
