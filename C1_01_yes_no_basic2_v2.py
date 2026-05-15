from RPS.C1_01_yes_no_basic2 import want_instructions
# functions go here

def yes_no(question):

    """ Checks user response to a question that is yes / no, returns 'yes' or 'no' """
    while True:
        
        response = input(question).lower()

        # check to see if the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

# Main routine

want_instructions = yes_no("Do you want to see the instructions? ").lower()
want_coffee = yes_no("Do you want coffee? ").lower()

print("we're done")