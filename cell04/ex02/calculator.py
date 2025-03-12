first_number = int(input("Give me the first number: "))
second_number = int(input("Give me the second number: "))
if second_number == 0:
    print("ERROR")
else:
    print("Thank you!")
    print(first_number,"+",second_number,"=",first_number+second_number)
    print(first_number,"-",second_number,"=",first_number-second_number)
    print(first_number,"/",second_number,"=",int(first_number/second_number))
    print(first_number,"*",second_number,"=",first_number*second_number)