# (5 points): As a developer, I want to make at least three commits with descriptive messages.
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

#Lists
destination_list = ["Tokyo", "Milan", "New York", "Los Angeles"]
restaurant_list = [ "Golden Palace", "Drunken Clam", "Purple Pheonix"]
transportation_list = ["A short stroll", "A horse-drawn carriage", "Our limousine service"]
entertainment_list = ["Night Bizaar", "Festival of Lights", "Louvre Immersive Experience"]

import random
destination = random.choice(destination_list)
restaurant = random.choice(restaurant_list)
transportation = random.choice(transportation_list)
entertainment = random.choice(entertainment_list)

print (destination)
print (restaurant)
print (transportation)
print (entertainment)

print(f"The Day Trip Generator has selected the perfect cozy getaway! You will be wisked away to the beautiful city of {destination}! Fine dining will follow at the illustrious {restaurant} and your entertrainment for the evening will be taking in all of the sights, sounds, and scents of the annual {entertainment} - a local favorite! Finally, commute in style! Your travel for the evening will be {transportation}. Is this your perfect getaway? ")