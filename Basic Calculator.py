calculating = True

while calculating == True:
    print("Do you have calculations to perform?")
    stillCalculating = input("Enter \"Yes\" or \"No\": ").upper()
    print()

    if stillCalculating == "YES":
        print("Please enter the type of calculation you want to perform.")
        calculationType = input("Enter \"Addition\", \"Subtraction\", \"Multiplication\", \"Division\": ").upper()
        print()
        
        try:
            num1 = float(input("Please enter the first number for the calculation: "))
            print()
            num2 = float(input("Please enter the second number for the calculation: "))
            print()
        except ValueError:
            print("Error: You did not enter a number")
            continue

        if calculationType == "ADDITION":
            print("Sum: ", num1 + num2)
        elif calculationType == "SUBTRACTION":
            print("Difference: ", num1 - num2)
        elif calculationType == "MULTIPLICATION":
            print("Product: ", num1 * num2)
        elif calculationType == "DIVISION":
            print("dividend: ", num1 / num2)
        else:
            print("You did not enter \"Addition\", \"Subtraction\", \"Multiplication\", \"Division\"")

    elif stillCalculating == "NO":
        calculating = False
        print("Thanks for using my calculator")

    else:
        print("Error: You did not enter \"Yes\" or \"No\"")
    
    print()