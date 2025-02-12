# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. 
# The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that 
# the least significant digit of the number is the head. The function should return the head of a new linked listed
# representing the sum of the input lists. The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

def add_lists(head_1, head_2, carry=0):
  if head_1 is None and head_2 is None and carry == 0:
    return None 
  val1 = 0 if head_1 is None else head_1.val
  val2 = 0 if head_2 is None else head_2.val
  sum = val1 + val2 + carry
  carry = 1 if sum > 9 else 0
  digit = sum % 10
  node = Node(digit)
  next1 = None if head_1 is None else head_1.next
  next2 = None if head_2 is None else head_2.next
  node.next = add_lists(next1, next2, carry)
  return node 