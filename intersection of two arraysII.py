from typing import List
class solution:
    def intersections(self,nums1:List[int],nums2:List[int])->List[int]:
        # result = []
        # for num in nums1:
        #     if num in nums2:
        #         result.append(num)
        #         nums2.remove(num)
        #return result
        return list(filter(lambda x:x in nums2 and nums2.remove(x) is None,nums1))
z = solution()
print(z.intersections([9,4,4,9,2,3],[9,4,5]))