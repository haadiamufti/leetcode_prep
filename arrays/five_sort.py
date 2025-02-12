# Write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of 
# the list such that all 5s appear at the end. Your function should perform this operation in-place by mutating the 
# original list. The function should return the list.

# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.

def five_sort(nums):
  i = len(nums) - 1
  j = 0
  while j < i:
    while i>= 0:
      if nums[i] == 5:
        i -= 1
      else:
        break
    if nums[j] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i -= 1
    j += 1
  return nums

print(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])
# -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

)