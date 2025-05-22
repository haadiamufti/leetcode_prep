# Given an array arr[] of size n, the task is to find the prefix sum of the array. 
# A prefix sum array is another array prefixSum[] of the same size, such that prefixSum[i] is 
# arr[0] + arr[1] + arr[2] . . . arr[i].

# Input: arr[] = [10, 20, 10, 5, 15]
# Output: 10 30 40 45 60
# edge cases: [], ['a']
def prefix_sum(arr):
    prefix_sum = []
    prev_sum = 0
    for a in arr:
        prefix_sum.append(a+prev_sum)
        prev_sum = prefix_sum[-1]
    return prefix_sum


            
# Input :  arr[] = [1, 2, 3, 4], k = 8.
# Output : 2

        
