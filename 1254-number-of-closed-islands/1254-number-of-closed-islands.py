class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            # Stop if we go outside the grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Stop if the cell is water or already visited
            if grid[r][c] == 1:
                return

            # Mark this land cell as visited
            grid[r][c] = 1

            # Explore all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Remove all land connected to the boundary
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if grid[r][c] == 0:
                        dfs(r, c)

        # Count the remaining islands
        count = 0

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)

        return count