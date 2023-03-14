class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        # Col Pointers
        right = len(matrix[0])
        left = 0

        # ROW Pointers
        top = 0
        bottom = len(matrix)
        
        while left < right and top < bottom:

            # for left to right. fix top
            for i in range(left, right):
                res.append(matrix[top][i])    
            top+=1
            # top to bottom. fix right
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1
            
            if not(left < right and top < bottom):
                break

            # right to left. fix bottom
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            # bottom to top. fix left
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left+=1
        return res

        # IMPORTANT TO PLACE UPDATE ACCORDINGLY
        # T(m*n)
        # S(1)