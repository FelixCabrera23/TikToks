def maxProfit(prices):
    # This cheks if the list is too short
    if len(prices)<2:
        return 0
    
    best = 0 #set best profit
    buy = prices[0]
    
    for day in prices[1:]:
        if day < buy : buy = day
        profit = day - buy
        if profit > best: best = profit

    return best