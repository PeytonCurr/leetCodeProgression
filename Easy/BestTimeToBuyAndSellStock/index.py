#My Optimal Sliding Window Solution - Time: O(n) Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDif = 0
        l,r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            if prices[r] > maxDif + prices[l]:
                maxDif = prices[r] - prices[l]
            r += 1
        return maxDif