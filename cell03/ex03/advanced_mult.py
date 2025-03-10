number = 0
while number < 11:
    count = 0
    print(f"Table de {number}: ", end="")
    while count < 11:
        print(number * count, end=" ")
        count += 1 
    print() # for new line
    number += 1 