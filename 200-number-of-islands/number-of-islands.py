class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        numisl=0

        for i in range (len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    self.dfs(grid, i,j)
                    numisl+=1
        return numisl

    def dfs(self, grid, r, c):
        #mark as visited 

        grid[r][c]="0"
        dirs=[(0,1), (0,-1), (1,0), (-1,0)]
        
        # we are checking for every cell so time complexity is O(mn)
        for dirc in dirs:
            i=r+dirc[0]
            j=c+dirc[1]

            if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0"):
                continue 
            self.dfs(grid, i,j)
            

