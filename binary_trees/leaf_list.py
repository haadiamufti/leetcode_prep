# Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the 
# values of all leaf nodes in left-to-right order.

class Node:
      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def leaf_list(root):
  leaves = []
  _leaf_list(root, leaves)
  return leaves
  
def _leaf_list(root, leaves):
  if root is None:
    return 
    
  if root.right is None and root.left is None:
    leaves.append(root.val)
    
  _leaf_list(root.left, leaves)
  _leaf_list(root.right, leaves)


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

print(leaf_list(a)) # -> [ 'd', 'e', 'f' ] 
