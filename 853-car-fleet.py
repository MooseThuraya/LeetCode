class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pair = []
        for p,s in zip(position, speed):
            pair.append([p,s])
        
        for p, s in sorted(pair)[::-1]:
            # target - pos / speed
            curTime = (target-p) / s

            if len(stack) == 0:
                stack.append([p,s,curTime])
                continue

            # check if curCar is slower? then it's another car fleet
            if curTime > stack[-1][2]:
                stack.append([p,s,curTime])
        
        return len(stack)
            
        # ANALYSIS
        # T(nlogn):  nlogn (sorting) + n (loop over new pair) -- > nlogn
        # S(n): stack is n at worst, OR sorting: n OR pair n

        # WHITEBOARD
        # 12-10 = 2/2 = 1
        

        # [[P,S], [p,s], [p,s]] # if it arrives faster or equal time, then it's one fleet

        # 12-8= 4/4 = 1

        # 12-5 = 7/1 = 7

        # 12-3 = 9/3 = 3

        # 12-0 = 12/1 = 12

            
            