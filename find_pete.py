#!/usr/bin/env python3
""" Text-based crime-solving game | Will Park """

# import necessary modules
import time
import sys

def main():

    user_name = input("Please enter your name: ").capitalize().strip()

    # game state information that decides the game progress and result
    curr_chapter = 1
    curr_time = "04:22 AM"
    curr_location = "Unknown"
    leads = []

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

    # prints the list of leads that the user has found during game
    def print_leads():
        leads_script = "----- Leads: " + leads + " -----"
        print_slowly(leads_script, 0.1)

    # prints the current chapter texts at a relatively fast pace 
    def print_game_text(text):
        print_slowly(text, 0.075)

    # prompts the user to enter their next move which will decide the next scenario
    def prompt_user_choice(l1, l2):
        print_slowly("...", 0.1)
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

    # prints introductory texts at the beginning of the game. Prints empty lines for better readability
    print()
    print()
    print_slowly("----- September 21, 2022 | Hershey, PA -----", 0.175)
    print_time()
    print_location()
    print()
    print_game_text("\"Bzzt... Bzzt... Bzzt...\"")
    print_game_text("--- You wake up. Your eyes are still blurry but you manage to find your cell phone underneath the pillow.")
    print()
    print_game_text("You: \"Hello?\"")
    print_game_text(f"Z: \"{user_name}, it's me, Z. Listen, I need you to come to the town square parking lot. Now.\"")

    # updates the game scenario time and location
    curr_time = "05:02 AM"
    curr_location = "Town Square Parking Lot"

    # prints game scenario until the final stage
    while curr_chapter < 4:
        print()
        print()
        print_time()
        print_location()
        # print the list of leads the user has gathered if its length is bigger than 0
        if (len(leads) > 0):
            print_leads
        print()

        # prints the game scenario for chapter 1
        if curr_chapter == 1:
            print_game_text("--- It's still dark in Hershey. The air is cold and crisp. And for some reason, feels heavy.") 
            print_game_text("--- You walk past police vehicles surrounding the parking lot.")
            print_game_text("--- You see Z standing next to a car.")
            print()
            print_game_text("You: \"What do we have here, Z?\"")
            print_game_text("Z: \"Someone called 911 an hour ago. They heard a gunshot in this parking lot.\"")
            print_game_text("You: \"And?\"")
            print_game_text("Z: \"When Sergeant Jones got here, he found the victim in this car.\"")
            print_game_text("You: \"Do we know who he is?\"")
            print_game_text("Z: \"Pete Peterson. 26. Male. Guy lives in Hummelstown.\"")
            print_game_text("You: \"What about the caller?\"")
            print_game_text("Z: \"We're still identifying them. Jones is on it.\"")
            print_game_text("You: \"I'll go to Hummelstown and see if I can find something there.\"")
            print_game_text("Z: \"Not right now. Chief wants you to meet the victim's parents.\"")
            
            # saves the user's choice for chapter 1
            user_res = prompt_user_choice("Go to Pete's apartment", "Meet Pete's parents")

            # update scenario info based on your's choice
            if user_res == 1:
                print_game_text("You: \"My guts are telling me I'll find something there. I'll call chief on the way there.\"")
                curr_location = "Hummelstown, PA"
                curr_time = "05:29 AM"

            if user_res == 2:
                print_game_text("You: \"Fine. I'll meet his parents and see if I can find something there.\"")
                curr_location = "Harrisburg, PA"
                curr_time = "05:41 AM"

        # prints the game scenario for chapter 2
        if curr_chapter == 2:

            if curr_location == "Hummelstown, PA":
                print_game_text("--- The neighborhood is still quite. It seems like everyone is still asleep.")
                print_game_text("--- You park your car and walk in to an old apartment building. The hallway is dead silent.")
                print_game_text("--- You talk to Pete's neighbors for a few hours, but nobody seems to know Pete very well.")
                print_game_text("--- You also check Pete's apartment room, but you do not find any lead there.")

            if curr_location == "Harrisburg, PA":
                print_game_text("--- The neighborhood is still quite. You are the only person on the road.")
                print_game_text("--- You park your car in front of Pete's parents' house.")
                print_game_text("--- You take a deep breath, and knock on the door.")
                print()
                print_game_text(f"You: \"Hi, I'm Detective {user_name} from HPD.\"")
                print()
                print_game_text("--- You talk to Pete's grieving parents for a few hours.")
                print_game_text("--- And learn that Pete called his parents last night.")
                print()
                print_game_text("Mrs. Peterson: \"He said he is meeting with someone.\"")
                print_game_text("You: \"Did he tell you who he was meeting?\"")
                print_game_text("Mrs. Peterson: \"Someone from work... he said 'she' is a friend from work.\"")
                print_game_text("You: \"She?\"")

                # add new lead about the co-worker
                leads.append('Linda')

            # update game scenario information for chapter 3
            curr_location = "Hershey Police Department"
            curr_time = "02:33 PM"

        # prints the game scenario for chapter 3
        if curr_chapter == 3:

            if len(leads) == 0:
                print_game_text("--- Someone walks into your office. It's Detective Z.")
                print()
                print_game_text("Z: \"What did his neighbors say?\"")
                print_game_text("You: \"They didn't know the victim that well. Any updates on the caller?\"")
                print_game_text("Z: \"We are still trying to identify them. They used a burner phone.\"")

            if len(leads) > 1:
                print_game_text("--- You are sitting in front of your computer. Detective Z walks in.")
                print()
                print_game_text("You: \"The victim's mother says he met someone from work last night. A co-worker.\"")
                print_game_text("Z: \"A co-worker?\"")
                print_game_text("You: \"Yes. A female. And I just looked at his file, there is only one female in his team.\"")

        # increment the current chapter count at the end of every chapter
        curr_chapter += 1

if __name__ == "__main__":
    main()