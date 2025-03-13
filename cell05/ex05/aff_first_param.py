user_input = input().split('" "')
i = 0
while i < len(user_input):
    user_input[i] = user_input[i].replace("'", "").replace('"', "")
    i += 1

if len(user_input) == 0:
    print("none")
else:
    print(user_input[0])
