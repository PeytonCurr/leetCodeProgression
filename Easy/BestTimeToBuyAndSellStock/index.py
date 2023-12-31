class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxP = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                newP = prices[right] - prices[left]
                if maxP < newP:
                    maxP = newP
            else:
                left = right
            right += 1
        return maxP