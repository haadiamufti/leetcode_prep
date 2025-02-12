# Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. 
# The function should merge the two lists together into single sorted linked list. The function should 
# return the head of the merged linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty and contain increasing sorted numbers.

class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

def merge_lists(head_1, head_2):
  tail = Node(None)
  current1 = head_1
  current2 = head_2
    
  while current1 is not None and current2 is not None:
    if current1.val < current2.val:
      tail.next = current1
      current1 = current1.next
    else:
      tail.next = current2
      current2 = current2.next
    tail = tail.next 
  if current1 is None:
    tail.next = current2
  if current2 is None:
    tail.next = current1

  if head_1.val < head_2.val:
    return head_1
  else:
    return head_2
  

