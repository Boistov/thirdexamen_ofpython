sentence = input()
word = 0
i = False

for j in sentence:
    if j != ' ':
        if not i:
            word += 1
            i = True
    else:
        i= False

print(word)
