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


# Main routine below

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]



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
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose: ", user_choice)

    # Ends game if user enters the exit code
    if user_choice == "xxx":
        break

    rounds_played += 1

    # If users are in infinite mode, increases number of rounds
    if mode == "infinite":
        num_rounds += 1




# Game loop ends here

# Game history / statistics area