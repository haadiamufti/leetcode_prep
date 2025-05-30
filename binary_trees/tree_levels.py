# Write a function, tree_levels, that takes in the root of a binary tree.
# The function should return a 2-Dimensional list where each sublist represents a level of the tree.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque
def tree_levels(root):
  if root is None:
    return []
  levels_list = []
  queue = deque([(root, 1)])
  while queue:
    current,level = queue.popleft()
    levels_list.append((current.val, level))
    if current.left is not None:
      queue.append((current.left, level+1))
    if current.right is not None:
      queue.append((current.right, level + 1))
      
  final_list = []
  for element in levels_list:
    value, level = element
    if level != len(final_list):
      final_list.append([])
    final_list[level-1].append(value)
  return final_list

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

print(tree_levels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]

