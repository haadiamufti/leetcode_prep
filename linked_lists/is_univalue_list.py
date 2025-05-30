# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. 
# The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

def is_univalue_list(head):
  current = head
  tracker = head.val
  while current is not None:
    if current.val != tracker:
      return False
    current = current.next
  return True 
  
    
