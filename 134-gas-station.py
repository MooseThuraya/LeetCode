class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start

        # Whiteboard
        # gas = [1,2,3,4,5]
        # cost = [3,4,5,1,2]
        # diff = [-2,-2,-2,3,3]

        # Why not the second 3?
        # explanation: The first three is an accumulation of the previos values, the second one is not, so we trust that it's the first also given that there is one guaranteed solution

        # T(n): one pass thru gas/cost
        # S(1): not using any extra space