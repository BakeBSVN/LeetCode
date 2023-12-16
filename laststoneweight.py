from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1st = max(stones)
            stones.remove(max1st)
            max2st = max(stones)
            stones.remove(max2st)
            if max1st > max2st:
                temp = max1st - max2st
                stones.append(temp)
        if len(stones) != 0:
            return(stones[0])
        return 0
def main():
    z = Solution()
    print(z.lastStoneWeight([2,7,4,1,8,1]))
if __name__ == '__main__':
    main()