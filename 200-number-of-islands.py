class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            # border, water, visited cases
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0' or grid[i][j] == 'v':
                return
            # cell is land
            grid[i][j] = 'v'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        rowLen = len(grid)
        colLen = len(grid[0])
        islandCount = 0
        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islandCount+=1
        return islandCount

        # T(n*m) where n rows and m columns are visited with dfs
        # S(n*m) where n rows and m columns are called in the call stack when grid is all 1's