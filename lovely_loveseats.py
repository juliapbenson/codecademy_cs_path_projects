# Project description: Lovely Loveseats, a furniture store, needs
# to build a system to help speed up the process of creating
# receipts for customers. 

# This program will store the names and prices of a furniture
# store’s catalog in variables.
# It then processes the total price and item list of customers,
# printing them to the output terminal.

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

sales_tax = .088

# Defines variables the program will use to create a running tally of a customer's expenses and a description of their purchases.
customer_one_total = 0

customer_one_itemization = ""

# Tracking customer expenses and purchases. 
customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

# Calculate sales tax on the customer's order
customer_one_tax = customer_one_total * sales_tax

# Calculate customer's total order 
customer_one_total += customer_one_tax

# Creates the customer's receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
