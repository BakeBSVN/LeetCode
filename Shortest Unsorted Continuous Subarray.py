from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if nums == sorted(nums):
                return 0
        else:
            while left != right:
                if nums[left] <= nums[right]:
                    if nums[left] == min(nums) and nums[right] == max(nums):
                        nums.pop(left)
                        right = len(nums)-1
                        nums.pop(right)
                        right-=1
                    elif nums[left] == min(nums) and nums[right] != max(nums):
                        nums.pop(left)
                        right-=1
                    elif nums[left] != min(nums) and nums[right] == max(nums):
                        nums.pop(right)
                        right-=1
                    elif nums[left] and nums[right] == min(nums):
                        nums.pop(right)
                        right-=1
                    elif nums[right] and nums[left] == max(nums):
                        nums.pop(left)
                    else:
                        return len(nums[left:right])+1
                else:
                            return(len(nums))