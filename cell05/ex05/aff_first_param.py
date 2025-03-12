user_input = input().split('" "')
user_inputs = [user_inputs.replace("'","").replace('"',"") for user_inputs in user_input]

if len(user_inputs) == 0:
    print("none")
else:
    print(user_inputs[0])