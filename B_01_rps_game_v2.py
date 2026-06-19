import random
# Checks that the user has entered a valid option based on a list
def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Gets user response and makes sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Checks to see if the user response is a word in the list
            if item == user_response:
                return item

            # Checks if the user response is the same as the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # prints error if user does not enter something that is valid
        print(error)
        print()

# Instructions
def instructions():

    """ Prints instructions """

    print("""
*** Instructions ***

To begin, choose the number of rounds you want to play (or play infinite mode).

The play against the computer. You need to enter either rock (r), paper (p), or scissors (s).

The rules are as follows:
•   Paper beats rock
•   Rock beats scissors
•   Scissors beats paper

Good luck!
    """)

# Checks for an integer above 0 or <enter>
def int_check(question):
   while True:
       """Checks user enters an integer more than / equal to 13"""
       error = "Please enter an integer above or equal to 1."

       to_check = input(question)

       # Checks for infinite mode
       if to_check == "":
           return "infinite"

       try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

       except ValueError:
           print(error)

# Compares user / computer choice and returns result (win / lose / tie)
def rps_compare(user, comp):

    # If user and computer have the same choice, it's a tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"

    # If it's not a tie / win, then it's a loss
    else:
        round_result = "lose"

    return round_result

# Game history
def display_history():
    # Calculates statistics
    win_percent = games_won / rounds_played * 100
    lose_percent = games_lost / rounds_played * 100
    tie_percent = games_tied / rounds_played * 100

    # Prints interesting history statistics (games played, wins/losses/ties, moves chosen, etc.)
    print(""
          "\n_______________________"
     "\n🪶📜 Game History 📜🪶"
      "\n_______________________")
    print(f"Rounds played: {rounds_played}")

    print(f"Wins: {win_percent:.2f}, Losses: {lose_percent:.2f}, Ties: {tie_percent:.2f}")

    print(f"Rock chosen: {rock_chosen}, Paper chosen: {paper_chosen}, Scissors chosen: {scissors_chosen}")




# Main routine below

# Initialise game variables
mode = "regular"
rounds_played = 0
games_won = 0
games_lost = 0
games_tied = 0
rock_chosen = 0
paper_chosen = 0
scissors_chosen = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []


print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()

# Asks the user if they want to see the instructions (check they say yes / no)
want_instructions = string_checker("Do you want to see the instructions? ")

# Displays the instructions here if the user wants to see them
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? (or push <enter> for Infinite Mode): ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Round headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n⨯⨯⨯ Round {rounds_played + 1} (Infinite Mode) ⨯⨯⨯"
        print(rounds_heading)
        print()

    if mode == "regular":
        rounds_heading = f"\n⨯⨯⨯ Round {rounds_played + 1}/{num_rounds} (Regular Mode) ⨯⨯⨯"
        print(rounds_heading)
        print()

    # Gets user choice
    user_choice = string_checker("User Choice: ", rps_list)

    # Tracks use of each choice for history statistics (I added for fun :)
    if user_choice == "rock":
        rock_chosen += 1
    elif user_choice == "paper":
        paper_chosen += 1
    elif user_choice == "scissors":
        scissors_chosen += 1

    # Ends game if user enters the exit code
    if user_choice == "xxx":
        break

    # Randomly chooses from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / won / tied counter and adds results to history
    if result == "win":
        games_won += 1
        feedback = "User Wins!"
    elif result == "lose":
        games_lost += 1
        feedback = "Computer Wins!"
    elif result == "tie":
        games_tied += 1
        feedback = "Game Tie!"
    else:
        feedback = "[Something went wrong!]"

    # Set up round feedback and outputs it to user
    # Add it to the game history list (including round name)
    round_feedback = (f"User: {user_choice}  Computer: {comp_choice}"
                      f"\n... {feedback}")
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)
    rounds_played += 1


    # If users are in infinite mode, increases number of rounds
    if mode == "infinite":
        num_rounds += 1




# Game loop ends here
print()
print("_______________________"
      "\n🎊🏆 Game Complete! 🏆🎊"
      "\n_______________________")
print()

# Game history / statistics area
view_history = string_checker("Would you like to view your game history? ")
if view_history == "yes":
    display_history()

# Program ends
print()
print("👋 Thank you for playing!")