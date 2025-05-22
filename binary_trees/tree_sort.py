# Given an array of n integers, return the k smallest elements in sorted order.

# You must not use built-in sorting functions like sorted() or .sort().
# Your solution should be as efficient as possible in both time and space, and must 
# not mutate the original list.

'''
Input: arr = [7, 2, 4, 8, 3, 1], k = 3  
Output: [1, 2, 3]

edge case: [], k> len(num_list)
'''
class Node:
    def __init__(self, value):
        self.val= value
        self.left = None
        self.right = None 
    
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
def inorder(root, result, k):
    if root is None or len(result) >= k:
        return 
    inorder(root.left,result, k)
    if len(result) < k:
        result.append(root.val)
    inorder(root.right, result, k)

def tree_sort(num_list, k):
    root = None
    for n in num_list:
        root = insert(root, n)
    result = []
    inorder(root, result, k)
    return result