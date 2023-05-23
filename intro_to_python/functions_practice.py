# Project description: Practice with Python functions.

# Creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the function as an input parameter
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))

# Removes all elements from a list with an index within a certain range
def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# We have a conveyor belt of items where each item is represented by a different number. 
# We want to know, out of two items, which one shows up more on our belt. 
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) > my_list.count(item2):
    return item1
  elif my_list.count(item1) == my_list.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Double a value at a given position in a list.
def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list

# Finds the middle item from a list of values. This will be different depending on whether there are an odd or even number of values. 
# In the case of an odd number of elements, we want this function to return the exact middle value. If there is an even number of elements, 
# it returns the average of the middle two elements.

def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]
  
print(middle_element([5, 2, -10, -4, 4, 5]))

# Counts how many numbers are divisible by ten from a list of numbers. 
def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i % 10 == 0:
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Automatically prints "Hello, name" where "name" is each person's name in a group.
def add_greetings(names):
  greeting = []
  for i in names:
    greeting.append("Hello, " + i)
  return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

# Repeatedly removes the first element of a list of numbers until it finds an odd number or runs out of elements.
def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Gives the values from a list at every odd index.
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))


# Uses nested loops in order to raise a list of numbers to the power of a list of other numbers.
def exponents(bases, powers):
  new_list = []
  for i in bases:
    for j in powers:
      new_list.append(i ** j)
  return new_list

print(exponents([2, 3, 4], [1, 2, 3]))

# Compares which list of two inputs has the larger sum and returns that list.
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for i in lst1:
    sum1 += i
  for j in lst2:
    sum2 += j
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

# Sums the elements of a list until the sum is greater than 9000, and then returns the sum. 
def over_nine_thousand(lst):
  sum = 0
  for i in lst:
    sum += i
    if sum > 9000: 
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# Manually implements .max() function. 
def max_num(nums):
  maximum = nums[0]
  for i in nums:
    if i > maximum:
      maximum = i
  return maximum

print(max_num([50, -10, 0, 75, 20]))

# Finds and prints out the indices in two equally sized lists where the numbers match.
def same_values(lst1, lst2):
  match = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      match.append(i)
  return match

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Tests two lists of the same length to see if the second list is the reverse of the first list.
def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# Returns the tenth power of a number
def tenth_power(num):
  return num ** 10

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# Returns the square root of a number
def square_root(num):
  return num ** (1/2)

print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# Calculates the percent of games won.
def win_percentage(wins, losses):
  total_games = wins + losses
  percent_won = 100 * (wins / total_games)
  return percent_won

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# Computes the average of two numbers
def average(num1, num2):
  return (num1 + num2) / 2

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# Returns the remainder of twice num1 divided by half of num2.
def remainder(num1, num2):
 return (num1 * 2) % (num2 / 2)

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# Prints out the first three multiples of a number and returns the third multiple.
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# Calculates the tip value given a total bill and tip percentage input. 
def tip(total, percentage):
  return (total * percentage) / 100

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# Prints out "James, James Bond" with 2 variables for your first and last name.
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# Calculates a dog's age in dog years. 
def dog_years(name, age):
  return name + ", " + "you are " + str(age * 7) + " years old in dog years"

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# This function is a chance to practice incorporating multiple operations in one function. 
def lots_of_math(a, b, c, d):
  sum_ab = a + b
  print(sum_ab)
  sub_cd = c - d
  print(sub_cd)
  times = sum_ab * sub_cd
  print(times)
  return times % a

print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
