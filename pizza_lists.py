# Project description: Create a program to organize a pizza restaurant's sales data using Python lists.

# List contains information on types of pizza the restaurant sells
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# List containing information about how much each kind of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

# Counts the number of $2 pizza slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Counts the number of types of pizza the restaurant sells
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")

# Creates a new list with sublists of pizza types and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sorts new list in order of increasing price
pizza_and_prices.sort()

# Stores the cheapest and most expensive pizzas in two different variables
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# Remove priciest_pizza from the pizza_and_prices list
pizza_and_prices.pop()

# Add a new pizza to the pizza_and_prices list
pizza_and_prices.insert(4, [2.5, "peppers"])

# Finds the cheapest 3 pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
