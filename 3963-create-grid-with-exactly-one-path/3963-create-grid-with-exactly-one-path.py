class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid =[["#"]*n for _ in range(m)]
        for i in range( len(grid)):
            for j in range(len(grid[0])):
                if i==0 or j==n-1:
                    grid[i][j] ="."
            grid[i] = "".join(grid[i])
        return(grid)