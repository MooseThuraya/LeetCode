class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Make sure interals are sorted
        intervals.sort()
        res = [intervals[0]]
        for i in range(len(intervals)):
            interval = intervals[i]
            curStart, curEnd = interval
            lastStart, lastEnd = res[-1]
            if curStart <= lastEnd:
                # they are overlapping
                
                # merge
                # take min start times
                minStartTime = min(curStart, lastStart)
                # max of end times
                maxEndTime = max(curEnd, lastEnd)
                # update last interval
                res[-1] = [minStartTime, maxEndTime]
            else:
                # not overlapping
                res.append(interval)
        
        return res

        # T(nlogn): where we have to sort intervals and linearly merge
        # S(n) if considering 'res' or intervals.sort()