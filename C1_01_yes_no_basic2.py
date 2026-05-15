
while True:
    want_instructions =input("Do you want to see the instructions? ").lower()

    # check to see if the user says yes / no
    if want_instructions == "yes" or want_instructions == "y":
        print("you ")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("fair")
        break
    else:
        print("please enter yes / no")
        continue

print("we're done")