month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (1000, 2000, 3000, 4000, 5000 , 6000, 7000, 8000, 9000, 10000, 11000, 12000)

max_profits = max(profits)
max_profits_index = profits.index(max_profits)
print(max_profits_index)

max_profits_month = month[max_profits_index]
print("The maximum profit is " + str(max_profits) + " this was recorded in the month of " + str(max_profits_month))

min_profits = min(profits)
min_profits_index = profits.index(min_profits)
print(min_profits_index)

min_profit_month = month[min_profits_index]
print("The minimum profit is " + str(min_profits) + " this was recorded in the month of " + str(min_profit_month))

