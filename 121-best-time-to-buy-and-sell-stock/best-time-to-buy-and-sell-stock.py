class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprice=0


        for i in range(len(prices)):
            minprice=min(prices[i],minprice)
            maxprice=max(maxprice,prices[i]-minprice)

        return maxprice
