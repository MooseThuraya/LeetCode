class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distList = []
        for point in points:
            dist = math.pow(point[0] - 0,2) + math.pow(point[1] - 0,2)
            distList.append((dist, point))
        
        kPoints = []
        heapq.heapify(distList)
        count = 0
        while count < k:
            _, point = heapq.heappop(distList)
            kPoints.append(point)
            count+=1
        return kPoints