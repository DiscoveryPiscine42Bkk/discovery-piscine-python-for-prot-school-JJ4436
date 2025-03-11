age = int(input("Please tell me your age: "))
count = 1
years = 10
print(f"You are currently {age} years old.")
while count < 4:
    print(f"In {years*count} years, you'll be {age+(years*count)} years old.")
    count +=1
    