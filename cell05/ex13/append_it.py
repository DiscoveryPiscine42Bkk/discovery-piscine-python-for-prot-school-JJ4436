sentence = input().split()
if len(sentence) == 0:
    print("none")
else:
    word_with_ism = []
    x = 0
    while x < len(sentence):
        if "ism" not in sentence[x]:
            word_with_ism.append(sentence[x] + "ism")
        x += 1
    print(*word_with_ism, sep="\n")
