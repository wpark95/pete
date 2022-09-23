#!/usr/bin/env python3
""" Text-based crime-solving game | Will Park """

# import necessary modules
import time
import sys

def main():

    # prompts the user to enter their name and prints empty lines for better readability
    user_name = input("Please enter your name to continue: ").capitalize().strip()
    print()
    print()

    # text display delay time (miliseconds)
    regular = 0.075
    slower = 0.1

    # current game information that decide the game progress and result
    curr_chapter = 1
    curr_time = "04:22 AM"
    curr_location = "Unknown"
    leads = []

    # prints text to the terminal with certain interval per letter, based on the delay argument
    def print_slowly(text, delay):
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # prints the current game scenario time, location, and leads (if not empty) using the print_slowly function
    def print_game_info():

        # print a line and an empty line for better readability before desplaying game info
        print("--------------------------------------------")
        print()
        
        # generates time and location info strings with their current state
        time_script = "----- Time: " + curr_time
        location_script = "----- Location: " + curr_location

        # generates leads info string if leads is not empty
        if len(leads) > 0:
            leads_script = "----- Leads: " + ','.join(leads)

        # prints time and location using prtin_slowly 
        print_slowly(time_script, slower)
        print_slowly(location_script, slower)

        # prints leads if leads is not empty
        if len(leads) > 0:
            print_slowly(leads_script, slower)

        # print an empty line and a line for better readability after desplaying game info
        print()
        print("--------------------------------------------")

    # reads the current chapter's .txt file and prints the current chapter texts at a relatively fast pace 
    def print_chapter_scenario(chapter_file):
        # prints an empty line for better readability before displaying each chapter scenario
        print()

        # reads in an appropriate chapter scenario text file based on the input (chapter_file)
        with open(f"{chapter_file}.txt", "r") as chapter:

            # iterates over the chapter
            for line in chapter:

                # replaces "user_name" in every line with the user_name input from the beginning of the game
                line = line.replace("user_name", user_name)

                # prints out each line using print_slowly function
                print_slowly(line, regular)

    # prompts the user to enter their next move which will decide the next scenario
    def prompt_user_choice(l1, l2):

        # prints prompt message
        print_slowly(".........................................", 0.005)
        print("--- What's your next move? (Enter 1 or 2)")
        print(".........................................")
        print("1 - " + l1)
        print("2 - " + l2)
        print(".........................................")

        # placeholder for user's choice
        user_choice = 0

        # keeps looping until user enters either 1 or 2
        while user_choice == 0:
            res = int(input(">>>>> "))
            if (res == 1):
                user_choice = 1
            elif (res == 2):
                user_choice = 2

        # returns user's choice
        return user_choice

    # prints intro chapter's texts at the beginning of the game
    print_slowly("    September 21, 2022 | Hershey, PA", 0.2)
    print()
    print_game_info()
    print_chapter_scenario('intro')
    
    # updates the game scenario time and location after intro
    curr_time = "05:02 AM"
    curr_location = "Hershey Town Square Parking Lot"

    # prints game scenario until the final chapter
    while curr_chapter < 4:

        # prints current game info (time, location, leads if not empty) and an empty line for readability
        print_game_info()

        # prints the game scenario for chapter 1
        if curr_chapter == 1:
            print_chapter_scenario('ch1-1')
            
            # saves the user's choice for chapter 1
            user_res = prompt_user_choice("Go to Pete's apartment", "Meet Pete's parents")

            # prints game texts and updates scenario info based on your's choice
            if user_res == 1:
                print()
                print_slowly("You: \"I feel like something's in Hummelstown. I'll call chief on the way.\"", regular)
                curr_location = "Hummelstown, PA"
                curr_time = "05:29 AM"

            if user_res == 2:
                print()
                print_slowly("You: \"But... alright, I'll talk to his parents.\"", regular)
                curr_location = "Harrisburg, PA"
                curr_time = "05:41 AM"

        # prints the game scenario for chapter 2
        if curr_chapter == 2:

            if curr_location == "Hummelstown, PA":
                print_chapter_scenario('ch2-1')

            if curr_location == "Harrisburg, PA":
                print_chapter_scenario('ch2-2')

                # add new lead about the co-worker
                leads.append('Linda')

            # update game scenario information for chapter 3
            curr_location = "Hershey Police Department - Your Office"
            curr_time = "10:33 AM"

        # prints the game scenario for chapter 3
        if curr_chapter == 3:

            if len(leads) == 0:
                print_chapter_scenario('ch3-1')

            if len(leads) > 0:
                print_chapter_scenario('ch3-2')

        # increments the current chapter count at the end of every chapter
        curr_chapter += 1

        # prints empty lines at the end of a chapter for better readability
        print()
        print()

if __name__ == "__main__":
    main()