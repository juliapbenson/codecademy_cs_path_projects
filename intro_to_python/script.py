# Project description: Create a simple recommendation 
# engine using Python. This engine will evaluate a person's 
# interests and then give them activity recommendations in their area. 

# Creates a list of the destinations this program will use.
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# Creates an example traveler who will use the recommendation engine.
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

# Returns the traveler's destination as a string
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Tests to make sure get_destination_index function is working
print(get_destination_index("Paris, France"))

# Returns destination index of the traveler
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Tests to see if get_traveler_location is working
print(get_traveler_location(test_traveler))

# Defines a list of attractions by first creating an empty list for each destination in destinations
attractions = []
for destination in destinations:
    attractions.append([])

# Tests to make sure the attractions list was created correctly
print(attractions)

# Adds an attraction to the attractions list
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
    except SyntaxError:
        return
    attractions_for_destination = attractions[destination_index]

# Tests to see if the add_attraction function is working correctly
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
print(attractions)

# Adds more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Finds attractions that match a person's interest and destination
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attr_in_city in attractions_in_city:
    possible_attraction = attr_in_city
    attraction_tags = attr_in_city[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

# Tests find_attractions function
la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)

# Prints out the list of attractions a traveler may be interested in
def get_attractions_for_traveler(traveler):
   traveler_destination = traveler[1]
   traveler_interests = traveler[2]
   traveler_attractions = find_attractions(traveler_destination, traveler_interests)
   interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
   for i in traveler_attractions:
      interests_string += i + " "
   return interests_string 

smills_france = get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]])
print(smills_france)
