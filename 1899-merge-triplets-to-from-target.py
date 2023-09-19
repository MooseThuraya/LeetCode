class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

        # T(n*3) => T(n) where we loop of n triplets and each triplet is always 3, so it's T(n)
        # S(3) => S(1) store at most 3 elements in set