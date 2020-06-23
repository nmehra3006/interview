def buy_sell_stocks(prices):

    min_price = float('inf')
    max_profit = 0
    for price in prices:

        cur_profit = price - min_price

        max_profit = max(max_profit, cur_profit)

        min_price = min(min_price, price)

    return max_profit




print buy_sell_stocks([7,1,5,3,6,4])