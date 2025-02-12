# Write a function, reverse_list, that takes in the head of a linked list as an argument. 
# The function should reverse the order of the nodes in the linked list in-place and return the new head of the
# reversed linked list.

class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
  previous = None 
  current = head
  while current is not None:
    temp = current.next
    current.next = previous 
    previous = current
    current = temp
  return previous 
    
