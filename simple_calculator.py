myName = input("Enter your name: ")
print(f"{myName} Welcome to the console calculator: ")
while True:
    print("\nAvailable operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    my_choice = input("Enter your choice: 1-6 ")
    # prompt them for the numbers to be used
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    if my_choice == "6":
       print("Thank you!")
       break
    elif my_choice == "1":
        print("Adding numbers")
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    else:
        print(f"{myName}, This is an Invalid choice")










