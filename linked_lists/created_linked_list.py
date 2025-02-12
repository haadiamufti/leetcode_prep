# Write a function, create_linked_list, that takes in a list of values as an argument.
# The function should create a linked list containing each item of the list as the values of the nodes. 
# The function should return the head of the linked list.

class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(values):
  head = Node(None)
  current = head
  for value in values:
    current.next = Node(value)
    current = current.next 
  return head.next 
    
