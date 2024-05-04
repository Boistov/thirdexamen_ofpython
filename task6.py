numbers = input().split()

n = {}
for i in numbers:
    if i in n:
        n[i] += 1
    else:
        n[i] = 1

for num in numbers:
    if n[num] == 1:
        print(num, end=' ')
