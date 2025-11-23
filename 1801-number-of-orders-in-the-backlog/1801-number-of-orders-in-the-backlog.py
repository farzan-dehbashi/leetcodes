class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []

        for price, amount, orderT in orders:
            if orderT == 0:
                while amount > 0 and sell and sell[0][0] <= price:
                    sellPrice, sellAmount = heapq.heappop(sell)
                    matched = min(amount, sellAmount)
                    amount, sellAmount = amount - matched, sellAmount - matched
                    if sellAmount > 0:
                        heapq.heappush(sell, (sellPrice, sellAmount))
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))
            else:
                while amount > 0 and buy and -buy[0][0] >= price:
                    buyPrice, buyAmount = heapq.heappop(buy)
                    matched = min(amount, buyAmount)
                    amount += -matched
                    buyAmount -= matched
                    if buyAmount > 0:
                        heapq.heappush(buy, (buyPrice, buyAmount))
                if amount>0:
                    heapq.heappush(sell, (price, amount))
        
        return (sum(x for _, x in buy) + sum(x for _, x in sell)) % (10**9+7)
                    