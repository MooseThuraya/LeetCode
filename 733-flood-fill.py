class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        startColor = image[sr][sc]
        def fill(startColor, i, j):
            if i >= len(image) or i < 0 or j >= len(image[0]) or j < 0 or image[i][j] == color or image[i][j] != startColor:
                return
            
            # we can proceed, because it is equal to the color we want to fill
            image[i][j] = color

            fill(startColor, i+1, j)
            fill(startColor, i, j+1)
            fill(startColor, i-1, j)
            fill(startColor, i, j-1)

        fill(startColor, sr, sc)
        return image