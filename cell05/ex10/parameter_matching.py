user_input = input("What was the parameter? : ")
def check_Hello(user_input):
    if user_input == "Hello":
        return print("Good job!")
    else:
        return print("Nope, sorry...")
check_Hello(user_input)