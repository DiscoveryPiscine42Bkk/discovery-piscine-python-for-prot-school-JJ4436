word = input()
word = word.split()
if len(word) == 0:
    print("none")
else:
    print(f"parameter: {len(word)}")
    for check in range(len(word)):
        print(f"{word[check]}: {len(word[check])}")