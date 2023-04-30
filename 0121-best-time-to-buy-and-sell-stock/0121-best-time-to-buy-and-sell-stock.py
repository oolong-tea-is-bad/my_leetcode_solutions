class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0, 1
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                newP = prices[r] - prices[l]
                maxP = max(maxP, newP)
            else:
                # Setting left to the lowest point
                l = r
            
            r += 1
        
        return maxP
    