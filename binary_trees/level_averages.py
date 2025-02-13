# Write a function, level_averages, that takes in the root of a binary tree that contains number values.
# The function should return a list containing the average value of each level.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def level_averages(root):
  if root is None:
    return []
  levels = []
  queue = deque([(root,1)])
  while queue:
    current,level = queue.popleft()
    if level != len(levels):
      levels.append([current.val])
    else:
      levels[level-1].append(current.val)
    if current.left is not None:
      queue.append((current.left, level+1))
    if current.right is not None:
      queue.append((current.right, level+1))
      
  levels = get_averages(levels)
  return levels 
  
import statistics
def get_averages(levels):
  avg_level = []
  for level in levels:
    avg_level.append(statistics.mean(level))
  return avg_level

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

print(level_averages(a)) # -> [ 3, 7.5, 1 ] 


  
