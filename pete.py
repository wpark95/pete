#!/usr/bin/env python3
""" Will Park |
    A text-based detective game
    Python Project 1 (If Logic Challenge) """

# import modules necessary for printing messages letter-by-letter in terminal
import time
import sys
# import crayons for text coloring and better readability
import crayons

def main():
    """ runtime code """

    # prompt the user to enter their name and save it as a variable for later use
    user_name = input("Please enter your name to continue: ").capitalize().strip()

    # current game information that decide the game progress and result. This will be constantly updated during game
    curr_chapter = 1
    curr_time = "04:22 AM"
    curr_location = "Hershey, PA"
    leads = []

    # print text to the terminal with certain interval per letter (default is 0.75)
    def print_slowly(text, delay=0.075):
        # iterate over the input text
        for letter in text:
            # write letters of the input text at certain interval (delay)
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        # print empty line for better readability
        print()

    # print the current game scenario time, location, and if not empty, leads, using the print_slowly function
    def print_game_info():
        # print dashes and an empty line for better readability before desplaying game info
        print(crayons.red("--------------------------------------------")) #colored red for readability
        print()       
        # print time and location info for the user, using prtin_slowly 
        print_slowly("----- Time: " + curr_time, 0.1)
        print_slowly("----- Location: " + curr_location, 0.1)
        # print leads if leads is not empty
        if len(leads) > 0:
            print_slowly("----- Leads: " + ','.join(leads), 0.1)
        # print an empty line and dashes for better readability after desplaying game info
        print()
        print(crayons.red("--------------------------------------------")) #colored red for readability

    # read the current chapter's .txt file and print the current chapter texts at a relatively fast pace 
    def print_chapter_scenario(chapter_file):
        # print an empty line for better readability before displaying each chapter scenario
        print()
        # open and read an appropriate chapter scenario text file
        with open(f"{chapter_file}.txt", "r") as chapter:
            # iterate over every line in the chapter
            for line in chapter:
                # make descriptive texts (start with "--- ") to be color blue for better readability
                if "--- " in line:
                    line = crayons.blue(line)
                # replace the word "user_name" in every line with the name user provided at the beginning
                line = line.replace("user_name", user_name)
                # print out each line in the terminal using print_slowly function
                print_slowly(line)

    # prompt the user to enter their next move between two options. The result decides the next scenario
    def prompt_user_choice(m1, m2):
        # print user choice prompt message and their next move options (dots are colored yellow for readability)
        print_slowly(crayons.yellow("........................................."), 0.005)
        print("--- What's your next move? (Enter 1 or 2)")
        print()
        print("1 - " + m1)
        print("2 - " + m2)
        print(crayons.yellow("........................................."))
        # placeholder for user's choice
        user_choice = 0
        # halt the program and keep prompting for user input until user enters either 1 or 2
        while user_choice == 0:
            res = int(input(">>>>> "))
            if res == 1:
                user_choice = 1
            elif res == 2:
                user_choice = 2
        # return user's choice
        return user_choice

    # print introductory texts at the beginning of the game
    print()
    print_slowly("          September 21, 2022", 0.2)
    print()
    print_game_info()
    print_chapter_scenario('intro')
    
    # update the game scenario time and location after intro
    curr_time = "05:02 AM"
    curr_location = "Hershey Town Square Parking Lot"

    # allow the user to continue playing the game until they reach the final chapter
    while curr_chapter < 4:

        # print current game info (time, location, and leads if not empty)
        print() # print empty line for better readability
        print_game_info()

        # if current chapter is chapter 1
        if curr_chapter == 1:
            # print the game scenario for chapter 1
            print_chapter_scenario('ch1')
            # prompt and save the user's move for chapter 1
            user_res = prompt_user_choice("Go to Pete's apartment", "Meet Pete's parents")
            # print related game texts and update scenario info for chapter 2, based on user's choice
            if user_res == 1:
                print()
                print_slowly("You: \"I feel like something's in Hummelstown. I'll call chief on the way.\"")
                curr_location = "Hummelstown, PA"
                curr_time = "05:29 AM"
            if user_res == 2:
                print()
                print_slowly("You: \"But... alright, I'll talk to his parents.\"")
                curr_location = "Harrisburg, PA"
                curr_time = "05:41 AM"

        # if current chapter is chapter 2
        if curr_chapter == 2:
            # print correct scenario for the current game location (decided by user's choice in previous chapter)
            if curr_location == "Hummelstown, PA":
                print_chapter_scenario('ch2-1')
            if curr_location == "Harrisburg, PA":
                print_chapter_scenario('ch2-2')
                # add new lead about the co-worker if user made the right choice
                leads.append('Linda')
            # update game scenario information for chapter 3
            curr_location = "Hershey Police Department - Your Office"
            curr_time = "10:33 AM"

        # if current chapter is chapter 3
        if curr_chapter == 3:
            # print correct scenario based on the length of leads (decided by user's choice in previous chapter)
            if len(leads) == 0:
                print_chapter_scenario('ch3-1')
            if len(leads) > 0:
                print_chapter_scenario('ch3-2')

        # increment the current chapter count at the end of every chapter
        curr_chapter += 1
        # print empty lines at the end of a chapter for better readability
        print()

if __name__ == "__main__":
    main()