from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        resuts = sorted([point[0] for point in points])
        ans = 0
        for i in range(1,len(resuts)):
            if resuts[i] - resuts[i-1] > ans:
                ans = resuts[i] - resuts[i-1]
        return ans