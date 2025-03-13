word = input().split()

if len(word) == 0:
    print("none")
else:
    print(f"parameter: {len(word)}")
    check = 0
    while check < len(word):
        word[check]= word[check].replace("'","").replace('"',"")
        print(f"{word[check]}: {len(word[check])}")
        check += 1
