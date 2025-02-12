# Write a function, breadth_first_values, that takes in the root of a binary tree. The 
# function should return a list containing all values of the tree in breadth-first order.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque
def breadth_first_values(root):
  if root is None:
    return []
  queue = deque([root])
  values = []
  while queue:
    current = queue.popleft()
    values.append(current.val)
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
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

print(breadth_first_values(a) )
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

