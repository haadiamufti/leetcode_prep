# Write a function, longest_streak, that takes in the head of a linked list as an argument.
# The function should return the length of the longest consecutive streak of the same value within the list.

class Node:
      def __init__(self, val):
        self.val = val
        self.next = None

def longest_streak(head):
  max = 0
  counter = 1
  current = head
  while current is not None:
    if current.next is not None and current.val == current.next.val:
      counter += 1
    elif counter > max:
      max = counter 
      counter = 1
    
    current = current.next

  return max
  
a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

print(longest_streak(a)) # 3

