# Imagine an island that is in the shape of a bar graph. When it rains, certain areas of the island fill up with 
# rainwater to form lakes. Any excess rainwater the island cannot hold in lakes will run off the island to the west 
# or east and drain into the ocean.

# Given an array of positive integers representing 2-D bar heights, design an algorithm (or write a function) 
# that can compute the total volume (capacity) of water that could be held in all lakes on such an island given an array 
# of the heights of the bars. Assume an elevation map where the width of each bar is 1.

# Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 15 (3 bodies of water with volumes of 1,7,7 yields total volume 
#                                                            of 15)

def volume_of_water(arr):
    volume = 0
    l, r = 0,len(arr)-1
    l_height = arr[0]
    r_height = arr[-1]
    while l < r:
        if l_height < r_height:
            left +=1
            l_height = max(arr[left], l_height)
            volume += l_height - arr[left]
        else:
            right -=1
            r_height = max(arr[right], r_height)
            volume += r_height - arr[right]
    return volume