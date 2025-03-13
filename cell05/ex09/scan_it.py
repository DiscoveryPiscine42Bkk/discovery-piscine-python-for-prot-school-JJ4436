import re

input = input().split()
check = 0

if len(input) <= 1:
    print("none")
else:
    while check < len(input):
        input[check] = input[check].replace("'", "").replace('"', "") 
        check += 1
    keyword = input[0]
    word = input[1::]
    check_word = re.findall(keyword, str(word))
    print(len(check_word))