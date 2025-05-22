# You are designing the screen lock feature for a device that displays an 
# n x m grid of dots (think of a pattern lock on an Android phone).

# Your task is to count the number of distinct valid patterns a user can draw by 
# connecting the dots, following these constraints:

# Constraints:
# A pattern starts at any dot in the grid.
# From any current dot, you can move up, down, left, or right to an adjacent dot (no diagonal moves).
# Each dot can be used only once in a single pattern (no revisiting).
# A pattern must be at least 1 dot long, and can include up to all n×m dots.

def count_patterns(n: int, m: int) -> int:
    if n < 1 or m < 1:
        return 0
    
    count = 0
    directions = [(1,0), (0,1), (-1,0), (0,-1)]    
    def dfs(i, j):
        nonlocal count
        
        if i < 0 or j < 0 or i > n-1 or j > m - 1:
            return 
        
        if (i,j) in visited:
            return 
        
        visited.add((i, j))
        count += 1
        
        for dx,dy in directions:
            dfs(i+dx, j+dy)
                
        visited.remove((i, j))
    
    for i in range(n):
        for j in range(m):
            visited = set()
            dfs(i,j)
    return count
    
# Complexity O(nxm)!