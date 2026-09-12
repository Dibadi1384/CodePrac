class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        self.firstisland=deque()
        self.paths=[]
        finish=False

        #first we need for find the new island and add the nodes to island one
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #start the dfs search from here
                if grid[r][c]==1:
                    self.dfs(grid, r, c)
                    finish=True
                    break
            if finish:
                break

        #now we do bfs on each island one cell
        return self.bfs(grid)

    
    def dfs(self, grid, r, c):
        #mark as visited
        grid[r][c]=2 
        self.firstisland.append([r,c])
        dirs=[(0,1), (0,-1), (1,0), (-1,0)]

        for d in dirs:
            i,j=r+d[0],c+d[1]

            #if out of bound or not island
            if (i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j]!=1):
                continue  
            self.dfs(grid,i,j)


    def bfs(self, grid):
        path = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        #index of first island cells
        while self.firstisland:
            #go through the first layer of island cells
            for _ in range(len(self.firstisland)):
                r, c = self.firstisland.popleft()
                #search for the water cells around  
                for d in dirs:
                    i, j = r + d[0], c + d[1]

                    if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]==2):
                        continue

                    if grid[i][j] == 1:
                        return path

                    #if cell is water cell, add it to what we need to travels and mark as traveled
                    if grid[i][j] == 0:
                        grid[i][j] = 2
                        self.firstisland.append([i, j])

            path += 1

        return -1






                    