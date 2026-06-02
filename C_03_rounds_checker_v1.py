# Check that users have entered a valid
# option based on a list
def int_check(to_check):
   while True:
       """Checks user enters an integer more than / equal to 13"""
       error = "Please enter an integer above or equal to 1."

       # Check for infinite mode
       if to_check == "":
           return "infinite"

       try:
            response = int(to_check)

            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

       except ValueError:
           return "invalid"
           # print(error)

# Automated testing is below in the form (test_case, expected_value)
to_test = [
    (1, 1),
    ("", "infinite"),
    (2, 2),
    (33, 33),
    ("0", "invalid"),
    ("0.5", "invalid"),
    ("1a", "invalid"),
    ("#", "invalid")
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_check(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
