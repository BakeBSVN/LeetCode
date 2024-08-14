from typing import List
class Solution:
        def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
            rows, clos = len(img),len(img[0])
            result = [[0]* clos for _ in range(rows)]
            for i in range(rows):
                for j in range(clos):
                    sum = img[i][j]
                    count = 1
                    if i > 0 and j > 0:
                        sum += img[i-1][j-1]   
                        count+=1
                    if i>0:
                        sum += img[i-1][j]
                        count+=1
                    if i>0 and j<clos-1:
                        sum+= img[i-1][j+1]
                        count+=1
                    if j > 0:
                        sum += img[i][j-1]
                        count+=1
                    if j < clos-1:
                        sum += img[i][j+1]
                        count+=1
                    if i < rows-1 and j > 0:
                        sum += img[i+1][j-1]
                        count+=1
                    if i < rows-1:
                        sum += img[i+1][j]
                        count+=1
                    if i < rows-1 and j < clos -1:
                        sum += img[i+1][j+1]
                        count+=1
                    result[i][j] = sum // count
            return result