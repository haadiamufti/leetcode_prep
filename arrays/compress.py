# Write a function, compress, that takes in a string as an argument. The function should return a compressed version 
# of the string where consecutive occurrences of the same characters are compressed into the number of occurrences
# followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

def compress(s):
  compressed = []
  
  i = 0
  while i < len(s):
    tracker = s[i]
    counter = 1
    j = i + 1
    while j < len(s) and s[j] == tracker:
      counter +=1
      j += 1
    compressed.append((s[i],counter))
    i = j 
  print(compressed)
  compressed_str = ''
  for pair in compressed:
    key, value = pair
    if value == 1:
      compressed_str += f'{key}'
    else:
      compressed_str += f'{value}{key}'
  return compressed_str
