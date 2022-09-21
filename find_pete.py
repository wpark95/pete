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

    while curr_step < 4:
        print_time()
        print_location()
        print()

        if curr_day == 1:
            print_game_text("--- It's still dark in Hershey. The air is cold and crisp, and, for some reason, heavy.") 
            print_game_text("--- More and more police vehicles are arriving at the scene.")
            print_game_text("You: \"Any updates, detective?\"")
            print_game_text("Z: \"Forensics just came in. Victim is 32 year-old. Male.\"")
            print_game_text("You: \"Name?\"")
            print_game_text("Z: \"Pete. Guy lives in Hummelstown.\"")
            print_game_text("You: \"Any leads?\"")
            curr_location = "Hummelstown, PA"
            curr_time = "06:48 AM"

        if curr_step == 2 and curr_location == "Hummelstown, PA":
            print_game_text("--- The neighborhood is still quite. You are the only person on the road.")
            print_game_text("--- You walk in to an apartment building, take a deep breath, and knock on a door.")

        curr_step += 1

if __name__ == "__main__":
    main()