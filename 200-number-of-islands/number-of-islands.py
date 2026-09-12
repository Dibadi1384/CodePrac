class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    self.dfs(grid,r,c)
                    islands+=1
    

        return islands

    
    def dfs(self, grid, r, c):
        #first mark as visited
        grid[r][c]="0"

        dirs=[(0,1), (0,-1), (1,0), (-1,0)]
        
        for dirc in dirs:
            i,j=r+dirc[0],c+dirc[1]

            #if out of bound or zero
            if (i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j]=="0"):
                continue
            
            #otherwise if one do a dfs on that node as a root
            self.dfs(grid,i,j)
        