import sys
from typing import List
import math
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    class Solution:
        def findmaxaverage(self,nums:List[int],k:int)->float:
            max = -math.inf
            temp = k
            if k ==1:
                return max(nums)
            else:
                for i in range(len(nums)):
                    sums = sum(nums[i:temp])/k
                    if sums>max and len(nums[i:temp])==k:
                        max = sums
                        temp+=1     
            return max
    data = Solution()
    nums =eval(input())
    k = int(input())
    print(data.findmaxaverage(nums,k))
def main():
    Input()
    Solve()
if __name__ == '__main__':
    main()