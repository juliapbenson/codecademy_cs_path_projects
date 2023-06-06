# Project description: You're creating a new robotics company. 
# Your idea is to create micro driving robots which are able to pick up 
# and deliver objects. This program begins to program the logic behind the driving robots. 

# Define the DriveBot class
class DriveBot:
    # Class variables
    all_disabled = False
    latitude = -999999
    longtitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # Assigns an `id` to the robot when it is constructed by incrementing the counter 
        # and assigning the value to `id`
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
        

    def control_bot(self, new_speed, new_direction):
       self.motor_speed = new_speed
       self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

# Create instances of DriveBot to test the methods
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.sensor_range = 10
robot_1.direction = 90
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change DriveBot class variables
DriveBot.longitude = 50
DriveBot.latitude = -50
DriveBot.all_disabled = True
print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)
