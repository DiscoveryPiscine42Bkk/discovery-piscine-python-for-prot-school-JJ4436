word = input().split('" "')
user_inputs = [user_inputs.replace("'","").replace('"',"") for user_inputs in word]

print(*user_inputs[::-1], sep='\n')
