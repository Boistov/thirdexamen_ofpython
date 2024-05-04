numbers = input().split()

num = None
for num in numbers:
    num = int(num)
    if num % 2 != 0:
        if num is None or num > num:
            num = num

if num is None:
    print(0)
else:
    print(num)
