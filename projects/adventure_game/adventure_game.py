# Importing necessary libraries
import random
import time
import string

# list for random dress
dresses = ["yellow", "red", "blue", "purple"]

# list for random place
places = ["restroom", "rooftop", "keyshop"]

# list of escapes
escape = ["mirror", "puddle", "wall"]


# Function to change randomly dress and place
def random_change():
    global dress
    global place
    dress = random.choice(dresses)
    place = random.choice(places)


# Function to simulate typewriting
def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.3)
        time.sleep(.03)
    print('')


# Compound statements
# Function that prints out each statement after a given time
def message_pause(message, delay=0):
    colors = {
        'red': '\033[91m',
        'purple': '\033[95m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'green': '\033[92m',
        'orange': '\033[33m',
        'yellow': '\033[93m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'black': '\033[0m'
    }
    chosen_color = random.choice(list(colors.values()))
    time.sleep(delay)
    typewriter_simulator(chosen_color + message)


# Input function
# Gives players some choices
def choices(prompt, choice1, choice2):
    while True:
        response = input(prompt).lower()
        if choice1 == response:
            break
        elif choice2 == response:
            break
        else:
            message_pause("Sorry, that's not a valid choice.")
    return response


# Introduction function
def intro():
    message_pause("You are in the Analyst's Office")
    message_pause("Analyst: 'Thomas, You seem "
                  "particularly triggered right now.'")
    message_pause("Analyst: 'Can you tell me what happened?'")
    message_pause("Thomas: 'I've had dreams that weren't just dreams.'")
    message_pause("In the meanwhile, Thomas has "
                  "some flashes and visions of a presumably past life.")
    message_pause("Thomas: 'Am I crazy?'")
    message_pause("The Analyst is writing down notes, "
                  "than he looks at Thomas.")
    message_pause("Analyst: 'We don't use that word in here!'")
    message_pause("Analyst: 'You've lost the capacity "
                  "to discern reality from fiction.'")
    message_pause("Analyst: 'That's why we have these meetings, "
                  "so I can help you distinguish "
                  "what is real and what is not.'")
    message_pause("Analyst: 'And also because we "
                  "don\'t want anyone to get hurt.'")
    message_pause("The Analyst prescribes some pills "
                  "to Thomas, and advise him to stay at home and rest.")
    message_pause("The next day Thomas wakes up, and prepare to go to work.")
    message_pause("After arriving at the office, Thomas "
                  "start to work with its Computer.")
    message_pause("A popup shows on the screen with a "
                  "message, alerting that a file is missing.")
    message_pause("At the same moment, the firealarm activates "
                  "and employees are forced to leave the building.")
    message_pause("As Thomas starts to leave the building "
                  "he receives an sms, from an unknown source "
                  f"telling Thomas to meet the source at the {place}.")
    message_pause("When he arrives, a misterious figure appeares with "
                  f"a {dress} suit, presenting himself as Morpheus.")
    message_pause("Morpheus: 'At last.'")
    message_pause("Thomas is confused.")
    message_pause("Thomas: 'I know you, you're a "
                  "character of my videogame.'")
    message_pause("Thomas: 'You can't be real.'")
    message_pause("Thomas: 'You can't be a character that I coded.'")
    message_pause("Morpheus: 'I'm more real than you might think Neo.'")
    message_pause("Thomas: 'Why do you call me Neo?'")
    message_pause("Morpheus: 'All your questions will "
                  "be answered once you make a choice.'")
    message_pause("Morpheus shows two pills to Neo. A red one and blue one.")
    message_pause("Morpheus: 'You've been living in a dream world.'")
    message_pause("Morpheus: 'It\'s time to choose Neo: "
                  "Blue pill, you return to your annoying "
                  "and repetitive life. Red pill, you "
                  "exit the Matrix and return to the real world.'")


# Function that let you choose
def get_choice():
    choice = choices("Choose Your pill: ", "red", "blue")
    if ("red" in choice):
        message_pause("Neo choses the Red pill.")
        if (place == "restroom"):
            message_pause(f"The {escape[0]} in the restroom starts to wafe.")
            message_pause(f"Morpheus invite Neo to enter the {escape[0]}.")
            message_pause(f"Neo enters the {escape[0]}.")
        elif (place == "rooftop"):
            message_pause(f"A {escape[1]} of whater starts to wafe.")
            message_pause(f"Morpheus invite Neo to enter the {escape[1]}.")
            message_pause(f"Neo enters the {escape[1]}.")
        elif (place == "keyshop"):
            message_pause(f"A {escape[2]} starts to wafe.")
            message_pause(f"Morpheus invite Neo to enter the {escape[2]}.")
            message_pause(f"Neo enters the {escape[2]}.")
        message_pause("Neo immediately wakes up in a Pod.")
        message_pause("Neo just woke up.")
        message_pause("His adventures continues in the real world.")
    elif ("blue" in choice):
        message_pause("Neo choses the Blue pill.")
        message_pause("Morpheus: 'I'm sorry Neo, but you're "
                      "not ready to leave the Matrix.'")
        message_pause(f"Security guards arrive at the {place} "
                      "and start to shoot at Morpheus.")
        message_pause("While Morpheus and the security guards are "
                      "fighting against eachother, Neo tries "
                      "to escape from the building.")
        message_pause("But suddenly, a black cat appeares in front of Neo.")
        message_pause("Neo starts to feel dizzy. After a "
                      "while he loses consciousness.")
        message_pause("A voice from nowhere says: "
                      "'Ahi ahi, it's deja vu again.'")


def enter_again():
    response = choices("Would you like to enter "
                       "the Matrix again? ", 'yes', 'no')
    if "no" == response:
        message_pause("OK, thanks for playing!")
        exit(0)


# Function that lets you play the game.
def enter_the_matrix():
    while True:
        random_change()
        intro()
        get_choice()
        enter_again()


if (__name__ == '__main__'):
    enter_the_matrix()
