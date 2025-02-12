# Questions solved from structy.net

# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most
# frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

from collections import Counter
def most_frequent_char(s):
  counts = Counter(s)
  return max(counts, key=counts.get )
most_frequent_char('bookeeper') # -> 'e'
