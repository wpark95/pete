#!/usr/bin/env python3
""" Finding Pete Game | Will Park """

import time
import sys

def main():

    curr_step = 1
    curr_time = "05:30 AM"
    curr_location = "Unknown"
    proof = []

    # slowly prints to the terminal (one letter at a time on the same line)
    def print_slowly(text, delay):
        if delay == None:
            delay = 0.15

        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def print_time():
        time_script = "--- Time: " + curr_time
        print_slowly(time_script, 0.15)

    def print_location():
        location_script = "--- Location: " + curr_location
        print_slowly(location_script, 0.15)

    def print_game_text(text):
        print_slowly(text, 0.1)

    def prompt_user_choice(l1, l2):
        print("--- What's your choice? Enter 1 or 2")
        print("1 - " + l1)
        print("2 - " + l2)
        user_choice = 0
        while user_choice == 0:
            res = int(input(">>>>> "))
            if (res == 1):
                user_choice = 1
            elif (res == 2):
                user_choice = 2
        return user_choice

    # print introductory texts
    print_slowly("--- September 21, 2022 | Hershey, PA", 0.2)
    print_time()
    print_location()
    print()
    print_game_text("Bzzt... Bzzt...")
    print_game_text("You: \"Hello?\"")
    print_game_text("Z: \"Hey, it's me, Z. Listen, we have an incident. We need you over here. Now.\"")
    print()
    print()
    curr_time = "06:02 AM"
    curr_location = "Town Square Parking Lot"

    while curr_step < 10:
        print_time()
        print_location()
        print()

        if curr_step == 1:
            print_game_text("--- It's still dark in Hershey. The air is cold and crisp, and, for some reason, heavy.") 
            print_game_text("--- More and more police vehicles are arriving at the scene.")
            print_game_text("You: \"Any updates, detective?\"")
            print_game_text("Z: \"Forensics just came in. Victim is 32 year-old. Male.\"")
            print_game_text("You: \"Name?\"")
            print_game_text("Z: \"Pete Larson. Guy lives in Hummelstown.\"")
            print_game_text("You: \"I will go talk to his neighbors.\"")
            print_game_text("Z: \"I will send the new guy there. Top wants you to meet the victim's parents.\"")
            user_res = prompt_user_choice("Go to Pete's apartment.", "Meet Pete's parents")
            if user_res == 1:
                curr_location = "Hummelstown, PA"
                curr_time = "06:32 AM"
            if user_res == 2:
                curr_location = "Harrisburg, PA"
                curr_time = "06:46 AM"
            curr_step += 1

        if curr_step == 2:
            if curr_location == "Hummelstown, PA":
                print_game_text("--- The neighborhood is still quite. You are the only person on the road.")
                print_game_text("--- You walk in to an apartment building. You notice a guy sleeping in the hallway.")

            if curr_location == "Harrisburg, PA":
                print_game_text("--- The neighborhood is still quite. You are the only person on the road.")
                print_game_text("--- You park your car in front of the only lit-up house in the neighborhood.")
                print_game_text("--- You take a deep breath and knock on the door")

            curr_step += 1

        curr_step += 1 # this is for during development (otherwise curr_step will never increment until fully developed)
        
if __name__ == "__main__":
    main()