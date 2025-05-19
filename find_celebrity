# Given a square matrix mat[][] of size n x n, such that mat[i][j] = 1 means ith person knows jth person, 
# the task is to find the celebrity. A celebrity is a person who is known to all but does not know anyone.
#  Return the index of the celebrity, if there is no celebrity return -1.

# Note: Follow 0-based indexing and mat[i][i] will always be 1.

def find_celebrity(matrix):
    if len(matrix[0]) == 1:
        return 0
    elif len(matrix) == 0:
        return -1
    #result = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and i!=j:
                break
        else:
            # check if everyone else knows i
            for k in range(len(matrix)):
                if k != i and matrix[k][i] != 1:
                    break
            else: 
                return i
    return -1
            
# edge case:
# [[]]
# [[1]]
# [[0,0],[0,0]] 
# mat[][] = [[1, 0, 1],  [0, 1, 0],  [0, 1, 1]]

