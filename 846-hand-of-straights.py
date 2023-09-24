class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = {}
        for h in hand:
            if count.get(h) is None:
                count[h] = 1
            else:
                count[h]+=1
        minH = list(count)
        heapq.heapify(minH)
        while len(minH) > 0:
            start = minH[0]
            for i in range(start, start + groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

# T(nlogn)
# S(n)