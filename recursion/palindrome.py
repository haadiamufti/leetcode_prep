# Write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is
# the same forwards and backwards.

# You must solve this recursively.

def palindrome(s):
    if s == '':
     return True
    return (s[0] == s[-1]) and palindrome(s[1:-1])

print(palindrome("pops") # -> False


)