import sys
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    n = int(input())
    nums = list(map(int,input().split()))
    sum = 0
    right = len(nums)
    left = 0
    while left!=len(nums):
        sum += max(nums[left:right])-min(nums[left:right])
        right-=1
        if right == left:
            left+=1
            right=len(nums)
    return sum
def main():
    Input()
    print(Solve())
if __name__ == '__main__':
    main()