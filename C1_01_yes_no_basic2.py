want_instructions =input("Do you want to see the instructions? ").lower()

# check to see if the user says yes / no
if want_instructions == "yes" or want_instructions == "y":
    print("you ")
elif want_instructions == "no" or want_instructions == "n":
    print("fair")
else:
    print("please enter yes / no")
