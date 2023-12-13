from art import *
from game_data import data
import random
import os

CELEB_DATA = data

def select_person(arr):
    # randomly select a person from the array
    index = random.randint(0,len(arr)-1)
    return arr[index]

def compare_followers(persona,personb,selection):
    # checks between two options if user selected the higher option
    persona_count = persona['follower_count']
    personb_count = personb['follower_count']
    a_person = persona
    b_person = personb
    if persona_count > personb_count:
        high = a_person
    else:
        high = b_person
    
    if selection == high:
        return True
    else:
        return False


def play_game(game_data):
    game_active = True
    score = 0

    # sets user
    person_a = select_person(game_data)
    person_b = select_person(game_data)
    while person_b == person_a:
        person_b = select_person(game_data) 

    # while user selects the correct person, the game will continue
    while game_active:
        print(f"\nCompare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
        print(vs)
        print(f"\nCompare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
        answer = input("\nWho has more followers? Type 'A' or 'B': ")
        if answer == 'A':
            selection = person_a
        else:
            selection = person_b

        if compare_followers(person_a,person_b,selection):
            score += 1
            # print(f"You're right! Your score {score}")
            person_a = selection
            person_b = select_person(game_data)
            while person_a == person_b:
                person_b = select_person(game_data) 
            os.system("clear")
            print(f"You're right! Your score {score}")
            
        else:
            print(f"\nSorry you lost! {person_a['name']} has {person_a['follower_count']} vs {person_b['name']} has {person_b['follower_count']}")
            print(f"Your final score is {score}")
            game_active = False
        
 

def main():
    
    print(logo)
    play_game(CELEB_DATA)

main()