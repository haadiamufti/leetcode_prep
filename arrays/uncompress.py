# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple
# groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an uncompressed version of the string where each 'char' of a group is repeated 
# 'number' times consecutively. You may assume that the input string is well-formed according to the previously
# mentioned pattern.

def uncompress(s):
  uncompressed = ''
  i = 0
  while i < len(s):
    print(i)
    if s[i] in '1234567890':
      num, index = get_num(s, i)
      uncompressed = uncompressed + (num * s[index])
      i = index
    i += 1
  return uncompressed

def get_num(s, i):
  num = ''
  for i in range(i, len(s)):
    if s[i] in '1234567890':
      num = num + s[i]
    else:
      num = int(num)
      return (num, i)
    
#print(get_num('n12e2z', 1))
print(uncompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'