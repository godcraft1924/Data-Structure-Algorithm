class Solution {
public:
    int m, n;
    vector<vector<vector<int>>> memo;

    bool solve(int i, int j, int openCount, vector<vector<char>>& grid) {

        if (grid[i][j] == '(')
            openCount++;
        else
            openCount--;

        if (openCount < 0)
            return false;

        int remaining = (m - i) + (n - j);

        if (openCount > remaining)
            return false;

        if (i == m && j == n)
            return openCount == 0;

        // Already calculated this state
        if (memo[i][j][openCount] != -1)
            return memo[i][j][openCount];

        bool res = false;

        // Down
        if (i + 1 <= m)
            res = solve(i + 1, j, openCount, grid) || res;

        // Right
        if (j + 1 <= n && !res)
            res = solve(i, j + 1, openCount, grid) || res;

        memo[i][j][openCount] = res;

        return res;
    }

    bool hasValidPath(vector<vector<char>>& grid) {

        m = grid.size() - 1;
        n = grid[0].size() - 1;

        if (grid[0][0] == ')' || grid[m][n] == '(')
            return false;

        if ((m + n + 1) % 2 == 1)
            return false;

        // openCount can never need to exceed m+n+1
        memo.assign(
            m + 1,
            vector<vector<int>>(
                n + 1,
                vector<int>(m + n + 2, -1)
            )
        );

        return solve(0, 0, 0, grid);
    }
};