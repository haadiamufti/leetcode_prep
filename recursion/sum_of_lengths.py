# Write a function sumOfLengths that takes in a list of strings and returns the total length of the strings.

# You must solve this recursively.

def sum_of_lengths(strings):
    if strings == []:
     return 0
    return len(strings[0]) + sum_of_lengths(strings[1:])

print(sum_of_lengths(['', ' ', '  ', '   ', '    ', '     ']) # -> 15

)