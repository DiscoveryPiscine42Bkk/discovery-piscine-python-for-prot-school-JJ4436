number_input = input().split()

if len(number_input) != 2:
    print("none")
else:
    try:
        start = int(number_input[0])
        end = int(number_input[1])
        
        numbers = []
        current = start
        while current <= end:
            numbers.append(current)
            current += 1

        print(numbers)
    except:
        print("none")
