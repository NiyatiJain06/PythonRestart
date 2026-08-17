#1- import the random module
import random

#2- create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kholi",
    "Nirmala Sitharamn",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

#3- start the healing generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no) ").strip().lower()
    if user_input == "no":
        break
    

#4- Print goodbye message
print("\nThanks for using the Fake News Headline Generator, Have a fun day!")