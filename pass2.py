while True:
    user_input = input("Enter number:")
    if user_input == 'q':
        print("Invalid digit")
        break
    elif user_input.isdigit():
        print("Valid digit")
    else:
        pass