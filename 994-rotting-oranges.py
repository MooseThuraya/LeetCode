class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rowLen = len(grid)
        colLen = len(grid[0])
        fresh = 0
        minutes = 0
        q = collections.deque()
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                # get current rotten orange in our level
                row, col = q.popleft()
                for dr, dc in directions:
                    # get candidate direction
                    r,c = row+dr, col+ dc
                    
                    # make sure its valid (borders, its fresh orange)
                    if r < 0 or r >= len(grid) or c < 0 or c >=len(grid[0]) or grid[r][c] != 1:
                        continue
                    
                    # current cell is valid

                    #set to rotten
                    grid[r][c] = 2
                    #add it to next level
                    q.append([r,c])
                    fresh-=1
            
            minutes+=1
        
        return minutes if fresh == 0 else -1


        # T(n*m) go thru n*m cells
        # S(n*m) fill queue as we traverse n*m cells