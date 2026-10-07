def intelligent_agent():

    low = 1
    high = 100
    attempts = 0

    print("===================================")
    print(" Intelligent Number Guessing Agent")
    print("===================================")
    print("Think of a number between 1 and 100.")
    print("Give feedback as: higher, lower, correct")

    while low <= high:

        # Agent selects the middle value
        guess = (low + high) // 2

        attempts += 1

        print("\nAgent's Guess:", guess)

        feedback = input(
            "Enter feedback (higher/lower/correct): "
        ).lower()

        if feedback == "correct":

            print("\nNumber found successfully!")
            print("Number:", guess)
            print("Total Attempts:", attempts)
            break

        elif feedback == "higher":

            # Secret number is greater than guess
            low = guess + 1

        elif feedback == "lower":

            # Secret number is smaller than guess
            high = guess - 1

        else:

            print("Invalid feedback!")
            print("Please enter higher, lower or correct.")

    else:

        print("\nInconsistent feedback!")
        print("The number could not be found.")


# Function call
intelligent_agent()