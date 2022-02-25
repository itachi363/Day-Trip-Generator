# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

from asyncore import loop
import random


destinations = ['Los Angelas', 'New York', 'Miami', 'Phoenix']

restaurants = ['Chipotle', 'Subway', 'Taco Bell', 'Mcdonalds']

transports = ['Bike', 'Car', 'Train', 'Plane']

entertainments = ['Movie', 'Fishing', 'Hiking', 'Biking']


def destination_gen(destination_lists):
    print("Welcome to day trip generator! If you aren't sure what you want to do for your vacation, you have come to the right place!")
    destination_rand = random.choice(destination_lists)
    looper = True
    question_one = input(f'We have selected {destination_rand} for your destination! Does this sound good? Enter y/n: ')
    while looper is True:
        if question_one == 'y':
            print("great let's move on")
            looper = False
            return destination_rand

        elif question_one == 'n':
            destination_rand = random.choice(destination_lists)
            question_one = input(f"Oh, sorry you don't like this destination. No worries, we can try something else! how about  {destination_rand}? Enter y/n: ")

        else:
            print("Error, try again")

destination_rand = destination_gen(destinations)     # make this for each list, then make a big print that summerizes the trip to the user



def restaurant_gen(restaurant_lists):
    restaurant_rand = random.choice(restaurant_lists)
    looper = True
    question_two = input(f'We have selected {restaurant_rand} for your destination! Does this sound good? Enter y/n: ')
    while looper is True:
        if question_two == 'y':
            print("great let's move on")
            looper = False
            return restaurant_rand

        elif question_two == 'n':
            restaurant_rand = random.choice(restaurant_lists)
            question_two = input(f"Oh, sorry you don't like this destination. No worries, we can try something else! how about  {restaurant_rand}? Enter y/n: ")

        else:
            print("Error, try again")

restaurant_rand = restaurant_gen(restaurants)



def transport_gen(transport_lists):
    transport_rand = random.choice(transport_lists)
    looper = True
    question_three = input(f'We have selected {transport_rand} for your destination! Does this sound good? Enter y/n: ')
    while looper is True:
        if question_three == 'y':
            print("great let's move on")
            looper = False
            return transport_rand

        elif question_three == 'n':
            transport_rand = random.choice(transport_lists)
            question_three = input(f"Oh, sorry you don't like this destination. No worries, we can try something else! how about {transport_rand}? Enter y/n: ")

        else:
            print("Error, try again")

transport_rand = transport_gen(transports)



def entertainment_gen(entertainment_lists):
    entertainment_rand = random.choice(entertainment_lists)
    looper = True
    question_four = input(f'We have selected {entertainment_rand} for your destination! Does this sound good? Enter y/n: ')
    while looper is True:
        if question_four == 'y':
            print("great let's move on")
            looper = False
            return entertainment_rand

        elif question_four == 'n':
            entertainment_rand = random.choice(entertainment_lists)
            question_four = input(f"Oh, sorry you don't like this destination. No worries, we can try something else! how about {entertainment_rand}? Enter y/n: ")

        else:
            print("Error, try again")

entertainment_rand = entertainment_gen(entertainments)


def flow_of_logic(logic_flow):
    flow_logic = logic_flow
    print(f'Destination:{destination_rand}')
    print(f'Transportation: {transport_rand}')
    print(f'Restaurant: {restaurant_rand}')
    print(f'Entertainment: {entertainment_rand}')

    question_five = input('Would you like to finalize your trip? Enter y/n: ')
    looper = True
    while looper is True:
        if question_five == 'y':
            print(f'Prepare for your dream vacation to come alive! You will be arriving in {destination_rand} by {transport_rand}, where you will spend the day {entertainment_rand}. You will end the evening dining in style at {restaurant_rand}, a famous local resteraunt.')
            looper = False
            return

        elif question_five == 'n':
            question_five = input('please run day trip planner again or answer y: ')

        else:
            print("Error, try again")

flow_logic = flow_of_logic(" ")
