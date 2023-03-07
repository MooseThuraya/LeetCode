class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visitedSet = set()
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        # store the prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
    
        def dfs(crs):
            # base for invalid linup
            if crs in visitedSet:
                return False
            if preMap[crs] == []:
                # this crs can be completed
                return True
            visitedSet.add(crs)
            # still unsure if we can complete
            for pre in preMap[crs]:
                if not dfs(pre):
                    # we cant complete
                    return False
            visitedSet.remove(crs)
            preMap[crs] = []
            return True
        
        # we have to call for every course, in case graph is not fully connected
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
        # T(n + p) where n is the numCourses, and p is the edges. We have to go thru all nodes and edges
        # S(n) either from call stack or visitedSet. Not O(n+p) because we do not store edges in a graph