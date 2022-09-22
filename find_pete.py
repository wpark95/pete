#!/usr/bin/env python3
""" Text-based truth-finding game | Will Park """

# import necessary modules
import time
import sys

def main():

    # game state information that decides the scenario
    curr_step = 1
    curr_time = "04:22 AM"
    curr_location = "Unknown"
    proof = []

    # prints text to the terminal with certain interval per letter
    def print_slowly(text, delay):
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # prints the current game scenario time using the print_slowly function
    def print_time():
        time_script = "----- Time: " + curr_time + " -----"
        print_slowly(time_script, 0.1)

    # prints the current game scenario location using the print_slowly function
    def print_location():
        location_script = "----- Location: " + curr_location + " -----"
        print_slowly(location_script, 0.1)

    # prints the current game texts for each scene at a relatively fast pace 
    def print_game_text(text):
        print_slowly(text, 0.05)

    # prompts the user to enter their next move which will decide the next scenario
    def prompt_user_choice(l1, l2):
        print()
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

    # prints introductory texts at the beginning of the game
    print_slowly("----- September 21, 2022 | Hershey, PA -----", 0.175)
    print_time()
    print_location()
    print()
    print_game_text("Bzzt... Bzzt... Bzzt...")
    print_game_text("--- You wake up. Your eyes are still blurry but you manage to find your cell phone underneath your pillow.")
    print()
    print_game_text("You: \"Hello?\"")
    print_game_text("Z: \"Hey, it's me, Z. Listen, I need you to come to the town square parking lot. Now.\"")
    curr_time = "05:02 AM"
    curr_location = "Town Square Parking Lot"

    # 
    while curr_step < 4:
        print()
        print()
        print_time()
        print_location()
        print()

        if curr_step == 1:
            print_game_text("--- It's still dark in Hershey. The air is cold and crisp. And for some reason, feels heavy.") 
            print_game_text("--- You walk past police vehicles surrounding the parking lot.")
            print_game_text("--- You see Z standing next to a car.")
            print()
            print_game_text("You: \"What do we have here, Z?\"")
            print_game_text("Z: \"Someone called 911 an hour ago. They heard a gunshot in this parking lot.\"")
            print_game_text("You: \"And?\"")
            print_game_text("Z: \"When Sergeant Jones got here, he found the victim in this car.\"")
            print_game_text("You: \"Do we know the victim?\"")
            print_game_text("Z: \"Pete. Pete Larson. Guy lives in Hummelstown.\"")
            print_game_text("You: \"I'll go to Hummelstown and see if I can find something there.\"")
            print_game_text("Z: \"Not right now. Chief wants you to meet the victim's parents.\"")
            user_res = prompt_user_choice("Go to Pete's apartment", "Meet Pete's parents")

            # Based on your's choice, update scenario info
            if user_res == 1:
                print_game_text("You: \"Z, my guts are telling me something's there. I'll call chief on my way there.\"")
                curr_location = "Hummelstown, PA"
                curr_time = "05:29 AM"
            if user_res == 2:
                print_game_text("You: \"Chief said that? Fine. I'll meet his parents and see if I can find something there.\"")
                curr_location = "Harrisburg, PA"
                curr_time = "05:41 AM"

        if curr_step == 2:
            if curr_location == "Hummelstown, PA":
                print_game_text("--- The neighborhood is still quite. You are the only person on the road.")
                print_game_text("--- You park your car and walk in to Pete's apartment building. The hallway is dead silent.")

            if curr_location == "Harrisburg, PA":
                print_game_text("--- The neighborhood is still quite. You are the only person on the road.")
                print_game_text("--- You park your car in front of the only lit-up house in the neighborhood.")
                print_game_text("--- You take a deep breath and knock on the door.")

        # increment the game progress (curr_step)
        curr_step += 1

if __name__ == "__main__":
    main()