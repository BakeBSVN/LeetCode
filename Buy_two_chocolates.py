class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
            prices = sorted(prices)
            min_max =prices[0]
            min_second = prices[1]
            res = money - (min_max+min_second)
            if res >= 0:
                return res
            return money
