
number_input = input().split()

if len(number_input) != 2:
    print("none")
else:
    try:
        start = int(number_input[0])
        end = int(number_input[1])
        
        numbers = [i for i in range(start, end + 1)]
        print(numbers)
    except:
        print("none")
