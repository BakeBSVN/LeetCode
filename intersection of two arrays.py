from typing import List
class solution:
    def intersections(self,nums1:List[int],nums2:List[int])->List[int]:
        return list(set(nums1).intersection(nums2))
z = solution()
print(z.intersections([3,1,2,3],[1,4,5]))