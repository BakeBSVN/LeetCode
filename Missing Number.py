from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set(nums)
        set2 = set1^set([y for y in range(0,len(nums)+1)])
        return list(set2)[0]