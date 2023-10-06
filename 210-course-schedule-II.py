class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        curVisited = set()
        completed = set()
        output = []
        preMap = {}
        
        if len(prerequisites) == 0:
            for i in range(numCourses):
                output.append(i)
            return output

        def dfs(crs):
            if crs in curVisited:
                return False
            if crs in completed:
                return True
            curVisited.add(crs)
            for preReq in preMap[crs]:
                if dfs(preReq) == False:
                    return False
            curVisited.remove(crs)
            completed.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            preMap[crs] = []
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)
        for crs in preMap:
            if dfs(crs) == False:
                return []
        return output
    
    # O(E+V)