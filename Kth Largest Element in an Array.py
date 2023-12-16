import sys
from typing import List
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            pass
def main():
    Input()
    Solve()
if __name__ == '__main__':
    main()