#!/usr/bin/env python3
""" Finding Pete Game | Will Park """

import time
import sys

def main():

    curr_day = 1
    curr_time = "05:30 AM"
    curr_location = "Unknown"
    playing = True
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

    def print_day():
        day_script = " DAY " + str(curr_day)
        print_slowly(day_script, 0.4)
        print()

    def print_game_text(text):
        print_slowly(text, 0.1)

    # print introductory texts
    print_slowly("--- September 21, 2022 | Hershey, PA", 0.2)
    print_time()
    print_location()
    print()
    print_game_text("Bzzt... Bzzt...")
    print_game_text("You: \"Hello?\"")
    print_game_text("Jay: \"Hey, it's me, Jay. Listen, we have an incident. We need you over here. Now.\"")
    print()
    print()
    curr_time = "06:02 AM"
    curr_location = "Hershey Town Square Parking Lot, 3F"

    while playing:
        print_day()
        print_time()
        print_location()
        print_game_text("--- It's still dark in Hershey. The air is cold and crisp, and for some reason, heavy.") 
        print_game_text("--- More and more police vehicles are arriving at the scene.")
        print_game_text("You: \"Any updates, detective?\"")
        print_game_text("Jay: \"Forensics just came in. Victim is 32 year old. Male.\"")
        print_game_text("You: \"Name?\"")
        print_game_text("Jay: \"Pete.\"")
        print_game_text("You: \"Text me his address. I will go talk to his neighbors.\"")
        location = "Hershey "

if __name__ == "__main__":
    main()