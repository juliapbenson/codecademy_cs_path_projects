# Project description: Creates simple Python functions to help solve physics problems. 

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Takes a temperature in Fahrenheit and converts it to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

# Takes a tempature in Celsius and converts it to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

# Function to compute force in Newtons
def get_force(mass, acceleration):
  force = mass * acceleration
  return force
train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function to compute E = m*c^2 in Joules
def get_energy(mass, c):
  energy = mass * (c ** 2)
  return energy

bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Function to compute the amount of work done in Joules
def get_work(mass, acceleration, distance):
  work = distance * get_force(mass, acceleration)
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " of work over " + str(train_distance) + " meters.")