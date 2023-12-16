import sys
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
        nums = list(map(int,input().split()))
        n = len(nums)
        if n == 1:
            return 0
        left, right = 0, n-1
        while left < n-1 and nums[left] <= nums[left+1]:
            left += 1
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
        if left >= right:
            return 0
        sub_min, sub_max = min(nums[left:right+1]), max(nums[left:right+1])
        while left > 0 and nums[left-1] > sub_min:
            left -= 1
        while right < n-1 and nums[right+1] < sub_max:
            right += 1
        return right - left + 1
    # left = 0
    # right = len(nums)-1
    # if nums == sorted(nums):
    #             return 0
    # while left != right:
    #     if nums[left] <= nums[right]:
    #         if nums[left] == min(nums) and nums[right] == max(nums):
    #             nums.pop(left)
    #             right = len(nums)-1
    #             nums.pop(right)
    #             right-=1
    #         elif nums[left] == min(nums) and nums[right] != max(nums):
    #             nums.pop(left)
    #             right-=1
    #         elif nums[left] != min(nums) and nums[right] == max(nums):
    #             nums.pop(right)
    #             right-=1
    #         elif nums[left] and nums[right] == min(nums):
    #             nums.pop(right)
    #             right-=1
    #         elif nums[right] and nums[left] == max(nums):
    #             nums.pop(left)
    #         else:
    #             return len(nums[left:right])+1
    #     else:
    #         return len(nums)
def main():
    Input()
    print(Solve())
if __name__ == '__main__':
    main()
    
# 1,3,2,2,2,2233333
# 2,
# 16,4,8,16,9,15
#2 4 6 8 9 43 3
# 2 2 2 2 6 6 6 6 6
# 2 2 2 2 6 4
# 2 2 2 2 4 3  6 6 6 6 6

# chia min max ra thanh 2 doan
# ở đoạn từ đầu đén max
# nếu len set = 1 thì bỏ qua và xét đoạn max
# ở đoạn max nếu sau max là min thì xét tiếp đén khi nào gặp 1 số  khác min và max thì kq sẻ là đoạn từ m
