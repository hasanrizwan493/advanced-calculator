print("Hello User!\nWelcome to My Calculator\nHow can i help you?\nAt this time I am capable of addition,subtraction,division , multiplication quare root, cube root, square a number, cube a number, random power of a number")
operations = ["addition", "subtraction", "division", "multiplication", "square root", "cube root", "square a number", "cube a number", "random power of a number"]
operation_input = str(input('Write name of operation you want to perform: '))
if operation_input in operations:
    permission = input(f"You have selected {operation_input} do you want to proceed with it(Yes or No): ")
    if permission == "yes":
        print('Ok proceed!')
        if operation_input == operations[0]:
            numbers = int(input("How many numbers you want to operate (Max3): "))
            if numbers == 1:
                First_no = int(input("Please enter your number(This number will be added to itself : "))
                result = First_no + First_no
                print(f"The answer to your operation is {result}")
            elif numbers == 2:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                result = First_no + Second_no
                print(f"The answer to your operation is {result}")
            elif numbers == 3:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                Third_no = int(input("Please enter your third number: "))
                result = First_no + Second_no + Third_no
                print(f"The answer to your operation is {result}")
            else: 
                print("Invalid amount of number!!")
                exit()
        elif operation_input == operations[1]:
            numbers = int(input("How many numbers you want to operate (Max3): "))
            if numbers == 1:
                print("One number cannot be subtracted to itself!!")
            elif numbers == 2:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                result = First_no - Second_no
                print(f"The answer to your operation is {result}")
            elif numbers == 3:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                Third_no = int(input("Please enter your third number: "))
                result = First_no - Second_no - Third_no
                print(f"The answer to your operation is {result}")
            else: 
                print("Invalid amount of number!!")
                exit()
        elif operation_input == operations[2]:
            numbers = int(input("How many numbers you want to operate (Max3): "))
            if numbers == 1:
                print("One number cannot be divided to itself!!")
            elif numbers == 2:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                result = First_no / Second_no
                print(f"The answer to your operation is {result}")
            elif numbers == 3:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                Third_no = int(input("Please enter your third number: "))
                result = First_no / Second_no / Third_no
                print(f"The answer to your operation is {result}")
            else: 
                print("Invalid amount of number!!")
                exit()
        elif operation_input == operations[3]:
            numbers = int(input("How many numbers you want to operate (Max3): "))
            if numbers == 1:
                print("Number will be multiplied to itself!!")
                First_no = int(input("Please enter the number: "))
                result = First_no * First_no
                print(f"The answer to your operation is {result}")
            elif numbers == 2:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                result = First_no * Second_no
                print(f"The answer to your operation is {result}")
            elif numbers == 3:
                First_no = int(input("Please enter first number: "))
                Second_no = int(input("Please enter second number: "))
                Third_no = int(input("Please enter your third number: "))
                result = First_no * Second_no * Third_no
                print(f"The answer to your operation is {result}")
            else: 
                print("Invalid amount of number!!")
                exit()
        elif operation_input == operations[4]:
            number = int(input("Please enter the number you want to find square root of: "))
            result = number ** 0.5
            print(f"The answer to your operation is {result}")
        elif operation_input == operations[5]:
            number = int(input("Please enter the number you want to find cube root of: "))
            result = number ** (1/3)
            print(f"The answer to your operation is {result}")
        elif operation_input == operations[6]:
            number = int(input("Please enter the number you want to find square  of: "))
            result = number ** 2
            print(f"The answer to your operation is {result}")
        elif operation_input == operations[7]:
            number = int(input("Please enter the number you want to find cube of: "))
            result = number ** 3
            print(f"The answer to your operation is {result}")
        elif operation_input == operations[8]:
            number = int(input("Please enter the base: "))
            power = int(input("Please enter the exponent: "))
            result = number ** power
            print(f"The answer to your operation is {result}")
        
    else:
        print("Thanks for coming!!")
        exit()
else:
    print("Invalid Operation")
    exit()
