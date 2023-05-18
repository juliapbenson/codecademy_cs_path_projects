# Project description: This program takes the weight of a package and determines the cheapest way to ship that package using the shipping company Sal's Shippers.

weight = 41.5
cost = 0

# The cost of premium shipping is a flat rate. 
premium_ship_cost = 125.00
print("Premium shipping costs $", premium_ship_cost)

# Print the cost of Ground Shipping for the package.

if weight <= 2:
  cost = 20 + 1.5 * weight
  print("Ground shipping costs $", cost)
elif weight > 2 and weight <= 6:
  cost = 20 + 3 * weight
  print("Ground shipping costs $", cost)
elif weight > 6 and weight <= 10:
  cost = 20 + 4 * weight
  print("Ground shipping costs $", cost)
elif weight > 10:
  cost = 20 + 4.75 * weight
  print("Ground shipping costs $", cost)

# Print the cost of drone shipping for the package. 

if weight <= 2:
  cost = 4.50 * weight
  print("Drone shipping costs $", cost)
elif weight > 2 and weight <= 6:
  cost = 9 * weight
  print("Drone shipping costs $", cost)
elif weight > 6 and weight <= 10:
  cost = 12 * weight
  print("Drone shipping costs $", cost)
else:
  cost = 14.25 * weight
  print("Drone shipping costs $", cost)