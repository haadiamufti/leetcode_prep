# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, 
# without reordering the remaining characters.

# Note: D can appear in any format (list, hash table, prefix tree, etc.

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct 
# output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right
# order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
from collections import Counter
def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    def is_subsequnce(s, w):
        i=j = 0
        while i < len(s) and j < len(w):
            if s[i] == w[j]:
                j += 1
            i += 1
        return j == len(w)
    max_length = float('-inf')
    max_word = ''
    for e in dictionary:
        if is_subsequnce(s,e):
            if len(e) == max_length:
                max_word = e if e < max_word else max_word 
            elif  len(e) > max_length:
                max_word = e
                max_length = len(e)

    return max_word