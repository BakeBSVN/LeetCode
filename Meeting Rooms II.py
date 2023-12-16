import sys
import heapq
import typing
## chua hoc
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    class Solution:
        def minMeetingRooms(self, intervals: typing.List[typing.List[int]]) -> int:
            if len(intervals) <= 1:
                return len(intervals)
            result = 1
            pq = []
            intervals.sort(key=lambda x: (x[0], x[1]))
            heapq.heappush(pq, intervals[0][1])
            for i in range(1, len(intervals)):
                if intervals[i][0] >= pq[0]:
                    heapq.heappop(pq)                   
                heapq.heappush(pq, intervals[i][1])
                result = max(result, len(pq))
            return result
    z = Solution()
    print(z.minMeetingRooms(eval(input())))
def main():
    Input()
    Solve()
if __name__ == '__main__':
    main()

