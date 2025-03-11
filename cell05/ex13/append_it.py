sentence = input().split()
if len(sentence) == 0:
    print("none")
else:
    word_with_ism = []
    for x in range(len(sentence)):
        if not "ism" in sentence[x]:
            word_with_ism.append(sentence[x] + "ism")
print(*word_with_ism, sep="\n")