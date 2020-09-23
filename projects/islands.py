from collections import deque


class Solution:
    numIslandsFound = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        width, height = len(grid[0]), len(grid)
        visited = [[False]* width for x in range(height)]
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1' and not visited[y][x]:
                    numIslandsFound += 1
                    self.markConnectedComponentsAsVisited(grid,visited,x,y)
        return self.numIslandsFound
    #start at x, y and mark connected components that are 1 as visited
    def markConnectedComponentsAsVisited(self,grid,visited,x,y):
        width, height = len(grid[0]), len(grid)
        stack = deque()
        stack.append((x,y))
        while len(stack) > 0:
            x,y = stack.pop()
            if visited[y][x]
                continue
            visited[y][x] = True
            if x - 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x-1, y))
            if x + 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x-1, y))
            if y - 1 >= 0 and grid[y-1][x] == '1'
                stack.append((x,y-1))
            if y + 1 < height and grid[y-1][x] == '1':
                stack.append((x,y+1))