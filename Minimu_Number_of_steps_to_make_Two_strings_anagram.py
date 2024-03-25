import sys
import math
threshold = 1e-9
from collections import Counter
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    class Solution:
        def minSteps(self, s: str, t: str) -> int:
            count = Counter(s)
            res = 0
            for c in t:
                if count[c] > 0:
                    count[c] -= 1
                else:
                    res += 1
            return res
    rs = Solution()
    print(rs.minSteps("friend", "family"))

def main():
    # Input()
    Solve()
if __name__ == '__main__':
    main()
    
