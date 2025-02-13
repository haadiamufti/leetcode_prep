# Write a function, bottom_right_value, that takes in the root of a binary tree. 
# The function should return the right-most value in the bottom-most level of the tree.

# You may assume that the input tree is non-empty.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
from collections import deque
def bottom_right_value(root):
  queue = deque([root])
  
  while queue:
    print(queue)
    current = queue.popleft()
    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)
    
  return current.val
  
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.right = d
d.left = e
e.right = f
print(bottom_right_value(a))