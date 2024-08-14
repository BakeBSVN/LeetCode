from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        return list(set1^set(map(int,range(1,len(nums)+1))))