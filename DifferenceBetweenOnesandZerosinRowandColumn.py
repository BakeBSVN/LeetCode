import sys
from typing import List
import math
threshold = 1e-9
def Input():
    try :
        # sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    # def sumr(grid):                                         
    #     OnesRowi = [sum(row) for row in grid]
    #     return OnesRowi
    # def sumcl(grid):
    #     onesCol = [sum(column) for column in zip(*grid)]
    #     return onesCol
    class Solution:
        def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
            swapped_matrix = [[1 if element == 0 else 0 if element == 1 else element for element in row] for row in grid]
            sumOnerow = sumr(grid) #[2,2,1]
            sumOneCl = sumcl(grid) #[1,1,3]
            sumZerorow = sumr(swapped_matrix) #[1,1,2]
            sumZerocl = sumcl(swapped_matrix) #[2,2,0]
            Ac
            for i in range(0,len(grid)):
                for j in range(0,len(grid[i])):
                    grid[i][j] = sumOnerow[i]+sumOneCl[j]-sumZerorow[i]-sumZerocl[j]
            return grid
    request = Solution()
    print(f'{request.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]])}')
def main():
    # Input()
    Solve()
if __name__ == '__main__':
    main()  