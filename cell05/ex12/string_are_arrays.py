sentence = input()
if sentence == "":
    print("none")
elif not "z" in sentence:
    print("none")
else:
    print("z"* sentence.count("z")) 