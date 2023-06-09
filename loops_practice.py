# Project description: Perform basic data analysis using Python loops. 

hairstyles = ["bouffant", "pixie", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 20, 20, 35, 50, 35]

last_week = [2, 3, 8, 4, 4, 6, 2]

total_price = 0

for i in prices:
  total_price += i

average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

new_prices = [i - 5 for i in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = []
for i in range(len(new_prices) - 1):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
print(cuts_under_30)
