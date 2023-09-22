class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = 0
        size = 0
        hashMap = {}
        output = []

        for i, curStr in enumerate(s):
            hashMap[curStr] = i

        for i, curStr in enumerate(s):
            end = max(hashMap[curStr], end)
            size+=1
            if i == end:
                output.append(size)
                size = 0
        return output

# T(n + n) = n
# S(26): english characters are atmost 26 (also not counting the output list)