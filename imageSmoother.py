import sys
import math
from typing import List
threshold = 1e-9
def Input():
    try :
        # sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        # sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    class Solution:
        def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
            rows, clos = len(img),len(img[0])
            result = [[0]* clos for _ in range(rows)]
            for i in range(rows):
                for j in range(clos):
                    sum = img[i][j]
                    count = 1
                    # i-1,j-1 top left
                    if i > 0 and j > 0:
                        sum += img[i-1][j-1]   
                        count+=1
                    # i-1,j top middle
                    if i>0:
                        sum += img[i-1][j]
                        count+=1
                    # i-1,j+1 top right
                    if i>0 and j<clos-1:
                        sum+= img[i-1][j+1]
                        count+=1
                    # i,j-1 left
                    if j > 0:
                        sum += img[i][j-1]
                        count+=1
                    # i,j+1 right
                    if j < clos-1:
                        sum += img[i][j+1]
                        count+=1
                    # i+1,j-1 down left
                    if i < rows-1 and j > 0:
                        sum += img[i+1][j-1]
                        count+=1
                    # i+1,j down middle
                    if i < rows-1:
                        sum += img[i+1][j]
                        count+=1
                    # i+1,j+1 down right
                    if i < rows-1 and j < clos -1:
                        sum += img[i+1][j+1]
                        count+=1
                    result[i][j] = sum // count
            return result
    s = Solution()
    print(f'{s.imageSmoother([[100,200,100],[200,50,200],[100,200,100]])}')
def main():
    Input()
    Solve()
if __name__ == '__main__':
    main()