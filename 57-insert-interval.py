class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0,len(intervals)):
            curStart = intervals[i][0]
            curEnd = intervals[i][1]
            newStart = newInterval[0]
            newEnd = newInterval[1]
            if curStart > newEnd:
                res.append(newInterval)
                return res + intervals[i:]
            elif newStart <= curEnd:
                #merge
                minStart = min(curStart, newStart)
                maxEnd = max(newEnd, curEnd)
                newInterval = [minStart, maxEnd]
            else:
                res.append(intervals[i])

        res.append(newInterval)
        return res