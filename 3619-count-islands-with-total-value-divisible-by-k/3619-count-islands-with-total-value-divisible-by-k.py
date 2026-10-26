class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)-1
        n = len(grid[0])-1
        print(m,n)
        def DFS(i,j):
            sum = grid[i][j]
            grid[i][j] = 0 

            direction = [[0,-1],[0,1],[-1,0],[1,0]]
            for p in direction :
                i_ = i + p[0]
                j_ = j + p[1]

                if (i_ >=0 and i_ <=m and j_ >=0 and j_<=n and grid[i_][j_]):
                    sum += DFS(i_,j_)
            return sum 
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0 :
                    sum  = DFS(i,j)
                    if sum%k == 0 :
                        count+=1 
        return count
                



        