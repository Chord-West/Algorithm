
profit = 0
min_num = 9999999

for price in prices:
    min_num = min(min_num, price)
    profit = max(profit, price - min_num)



