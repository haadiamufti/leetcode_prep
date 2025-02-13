
# Write a function, all_tree_paths, that takes in the root of a binary tree. 
# The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def _all_tree_paths(root):
  if root is None:
    return []
    
  if root.right is None and root.left is None:
    return [[root.val]]
    
  all_path = []
  
  left = _all_tree_paths(root.left)
  for path in left:
    path.append(root.val)
    all_path.append(path)
    
  right = _all_tree_paths(root.right)
  for path in right:
    path.append(root.val)
    all_path.append(path)

  return all_path

def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths
  

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

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 

